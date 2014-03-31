#!/usr/bin/env python2


import sys
from collections import namedtuple


Fmt = namedtuple('Fmt', 'reader writer')


def json():
    import json
    return Fmt(reader=json.load, writer=json.dump)


def yaml():
    import yaml
    return Fmt(reader=yaml.load, writer=yaml.dump)


def main():
    fmts = {
        'json': json,
        'yaml': yaml,
    }
    reader = fmts[sys.argv[1]]().reader
    writer = fmts[sys.argv[2]]().writer
    obj = reader(sys.stdin)
    writer(obj, sys.stdout)


if __name__ == '__main__':
    main()
