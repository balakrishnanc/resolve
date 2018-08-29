# About

Simple utility to resolve hostnames to IPv4 and IPv6 addresses using a list of free and public DNS resolvers.


# Installation

Use `pipenv` to install the dependencies.
```
§ pipenv install
```

# Usage

```
§ pipenv run python resolve/cli.py -h
usage: cli.py [-h] [--in input] [--out output] [host_name]

Resolve a list of DNS names to IP(v4/v6) addresses.

positional arguments:
  host_name     DNS name to resolve

optional arguments:
  -h, --help    show this help message and exit
  --in input    File with DNS names that need to be resolved
  --out output  Output file path
```