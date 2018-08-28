#!/usr/bin/env python
# -*- mode: python; coding: utf-8; fill-column: 80; -*-
#
# cli.py
# Created by Balakrishnan Chandrasekaran on 2018-08-28 11:31 +0200.
# Copyright (c) 2017 Balakrishnan Chandrasekaran <balakrishnan.c@gmail.com>.
#

"""
cli.py
Simple command-line utility to interact with the library.
"""

__author__  = 'Balakrishnan Chandrasekaran <balakrishnan.c@gmail.com>'
__version__ = '1.0'
__license__ = 'MIT'


import dns.resolver
import io
import resolvers
import sys


COMMA = ','


class Resolv:
    """Simple DNS resolver."""

    def __init__(self, resolvers):
        self._r = dns.resolver.Resolver()
        self._local = tuple(self._r.nameservers)
        self._resolvers = [self._local]
        self._resolvers.extend(resolvers)

    @classmethod
    def get_ips(self, reply):
        """Retrieve IP addresses from the answers."""
        return tuple([ip.to_text() for ans in reply.response.answer
                      for ip in ans.items])

    def run_query(self, query_fn, err_fn, *args):
        """Run query and invoke callback if errors were encountered."""

        # Context for throwing exceptions.
        _getErrContext = \
            lambda e: "query-<{}>-({}): {}".format(COMMA.join(self._r.nameservers),
                                              COMMA.join(args),
                                              str(e))
        try:
            return query_fn(*args)
        except dns.resolver.NXDOMAIN as e:
            sys.stderr.write("Error: {}\n".format(_getErrContext(e)))
            return err_fn()
        except dns.resolver.NoAnswer as e:
            sys.stderr.write("Warn: {}\n".format(_getErrContext(e)))
            return err_fn()
        except dns.exception.Timeout as e:
            sys.stderr.write("Error: {}\n".format(_getErrContext(e)))
            return err_fn()

    def q_A(self, name):
        """Resolve a DNS name to an IPv4 address ('A' query)."""
        return self.run_query(lambda *v: Resolv.get_ips(self._r.query(*v)),
                              lambda: tuple(),
                              name, 'A')

    def q_AAAA(self, name):
        """Resolve a DNS name to an IPv6 address ('AAAA' query)."""
        return self.run_query(lambda *v: Resolv.get_ips(self._r.query(*v)),
                              lambda: tuple(),
                              name, 'AAAA')

    def q_allA(self, name):
        """Resolve a DNS name to both an IPv4 and an IPv6 address."""
        for ns_pair in self._resolvers:
            # Change nameserver.
            self._r.nameservers = ns_pair

            yield (name, ns_pair, self.q_A(name), self.q_AAAA(name))

    def __repr__(self):
        num_ns = len(self._resolvers)

        show_ns = lambda r: r if len(r) == 2 else (r[0], '')
        ns_list = ', '.join(["<{};{}>".format(*show_ns(r))
                             for r in self._resolvers])
        return "[{}]: {}".format(num_ns, ns_list)

    @classmethod
    def Resolver(self):
        """Instantiate with a list of free and public DNS resolvers."""
        return Resolv([list(r.ips) for r in resolvers.REPO])


def read_names(f):
    """Read names, specified one per line, from a file."""
    return (line.strip() for line in io.open(f, 'r', encoding='utf-8'))


def main(args):
    # Sequence of names to be resolved.
    names = [args.host] if args.host else read_names(args.in_path)

    ip_list = lambda ips: ';'.join(ip for ip in ips)

    with args.out_file as out:
        r = Resolv.Resolver()
        for results in (r.q_allA(n) for n in names):
            for (name, ns, ips_v4, ips_v6) in results:
                out.write("{},{},{},{}\n".format(name,
                                                 ip_list(ns),
                                                 ip_list(ips_v4),
                                                 ip_list(ips_v6)))
                out.flush()


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description="Resolve a list of DNS names to IP(v4/v6) addresses.")
    parser.add_argument('host', metavar='host_name',
                        type=str,
                        nargs='?',
                        help='DNS name to resolve')
    parser.add_argument('--in', dest='in_path', metavar='input',
                        type=str,
                        required=False,
                        help='File with DNS names that need to be resolved')
    parser.add_argument('--out', dest='out_file', metavar='output',
                        type=str,
                        help='Output file path')

    args = parser.parse_args()
    if not (args.host or args.in_path):
        parser.print_help()
        sys.exit(1)

    if args.in_path and args.host:
        args.host = None
        sys.stderr.write('Warn: ignoring `host` specified in command-line!\n')

    if args.out_file:
        args.out_file = io.open(args.out_path, 'w', encoding='utf-8')
    else:
        args.out_file = sys.stdout

    main(args)
