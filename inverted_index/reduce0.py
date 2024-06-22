#!/usr/bin/env python3
"""Reduce 0."""

import sys
import itertools


def reduce_one_group(group):
    """Reduce one group."""
    doc_count = 0
    for line in group:
        _, count = line.strip().split("\t", 1)
        doc_count += int(count)
    print(f"{doc_count}")


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]


def main():
    """Divide sorted lines into groups that share a key."""
    for _, group in itertools.groupby(sys.stdin, keyfunc):
        # Input: document \t 1
        # Groups values by key
        reduce_one_group(group)


if __name__ == "__main__":
    main()
