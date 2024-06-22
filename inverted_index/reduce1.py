#!/usr/bin/env python3
"""Reduce 1."""

import sys
import itertools


def reduce_one_group(group):
    """Reduce one group."""
    for line in group:
        doc_id, content = line.strip().split("\t", 1)
        print(f"{doc_id}\t{content}")
        # Output: {doc_id}\t{content}


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]


def main():
    """Divide sorted lines into groups that share a key and reduce."""
    # input is {doc_id}\t{content}
    # group by doc_id
    for _, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(group)


if __name__ == "__main__":
    main()
