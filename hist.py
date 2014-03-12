#!/usr/bin/env python2

import sys
from collections import Counter
import argparse


def sorted_items(d):
    return sorted(d.items(), key=lambda x: x[1])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cumulative', '-c', action='store_true')
    args = parser.parse_args()

    counter = Counter()

    for line in sys.stdin:
        counter[line.strip()] += 1

    total = 0
    for line, count in sorted_items(counter):
        total += count
        if args.cumulative:
            print total, line
        else:
            print count, line


if __name__ == '__main__':
    main()
