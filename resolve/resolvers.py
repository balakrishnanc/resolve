#!/usr/bin/env python
# -*- mode: python; coding: utf-8; fill-column: 80; -*-
#
# resolvers.py
# Created by Balakrishnan Chandrasekaran on 2018-08-28 11:11 +0200.
# Copyright (c) 2017 Balakrishnan Chandrasekaran <balakrishnan.c@gmail.com>.
#

"""
resolvers.py
List of free and public DNS resolvers.
"""

__author__  = 'Balakrishnan Chandrasekaran <balakrishnan.c@gmail.com>'
__version__ = '1.0'
__license__ = 'MIT'


from collections import namedtuple as nt


# Nameserver details.
NS = nt('NS', ('ips', 'provider'))


# Repository of free and public DNS resolvers.
REPO = {
    NS(('209.244.0.3', '209.244.0.4'), 'Level3'),
    NS(('64.6.64.6', '64.6.65.6'), 'Verisign'),
    NS(('8.8.8.8', '8.8.4.4'), 'Google'),
    NS(('9.9.9.9', '149.112.112.112'), 'Quad9'),
    NS(('84.200.69.80', '84.200.70.40'), 'DNS.WATCH'),
    NS(('8.26.56.26', '8.20.247.20'), 'Comodo Secure DNS'),
    NS(('208.67.222.222', '208.67.220.220'), 'OpenDNS Home'),
    NS(('199.85.126.10', '199.85.127.10'), 'Norton ConnectSafe'),
    NS(('81.218.119.11', '209.88.198.133'), 'GreenTeamDNS'),
    NS(('195.46.39.39', '195.46.39.40'), 'SafeDNS'),
    NS(('69.195.152.204', '23.94.60.240'), 'OpenNIC'),
    NS(('208.76.50.50', '208.76.51.51'), 'SmartViper'),
    NS(('216.146.35.35', '216.146.36.36'), 'Dyn'),
    NS(('37.235.1.174', '37.235.1.177'), 'FreeDNS'),
    NS(('198.101.242.72', '23.253.163.53'), 'Alternate DNS'),
    NS(('77.88.8.8', '77.88.8.1'), 'Yandex.DNS'),
    NS(('91.239.100.100', '89.233.43.71'), 'UncensoredDNS'),
    NS(('74.82.42.42',), 'Hurricane Electric'),
    NS(('109.69.8.51',), 'puntCAT'),
    NS(('156.154.70.1', '156.154.71.1'), 'Neustar'),
    NS(('1.1.1.1', '1.0.0.1'), 'Cloudflare'),
    NS(('45.77.165.194', ''), 'Fourth Estate'),
    NS(('185.228.168.9', '185.228.169.9'), 'CleanBrowsing'),
}
