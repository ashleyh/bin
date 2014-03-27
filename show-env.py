#!/usr/bin/env python2

import sys

pid = sys.argv[1]
path = '/proc/{}/environ'.format(pid)

with open(path, 'rb') as f:
    buf = f.read()

for env in buf.split(b'\0'):
    print env
