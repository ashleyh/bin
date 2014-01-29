#!/usr/bin/env python2

import fcntl
import termios
import sys
import ctypes
import itertools
import subprocess


class WinSize(ctypes.Structure):
    _fields_ = (
        ('rows', ctypes.c_ushort),
        ('cols', ctypes.c_ushort),
        ('x_pixel', ctypes.c_ushort),
        ('y_pixel', ctypes.c_ushort),
    )


def get_rows():
    ws = WinSize()
    fcntl.ioctl(sys.stdout, termios.TIOCGWINSZ, ws)
    return ws.rows


def main():
    rows = get_rows()
    first_lines = list(itertools.islice(sys.stdin, rows))
    next_line = next(sys.stdin, None)
    if next_line is None:
        sys.stdout.writelines(first_lines)
    else:
        p = subprocess.Popen(["less"] + sys.argv[1:], stdin=subprocess.PIPE)
        p.stdin.writelines(first_lines)
        p.stdin.write(next_line)
        p.stdin.writelines(sys.stdin)
        p.stdin.close()
        p.wait()


if __name__ == '__main__':
    main()
