#!/usr/bin/env python3
"""Reduce 0."""

import sys
import itertools

# total_count = 0
# for line in sys.stdin:
#     key, value = line.strip().split("\t", 1)
#     if key == "document":
#         # Shouldn't ever be false anyways
#         total_count += int(value)


def reduce_one_group(line, group):
    """Reduce one group."""
    doc_count = 0
    for line in group:
        term, count = line.strip().split("\t", 1)
        doc_count += int(count)
    print(f"{doc_count}")

def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]


def main():
    """Divide sorted lines into groups that share a key."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        # Input: document \t 1
        # Groups values by key
        reduce_one_group(key, group)


if __name__ == "__main__":
    main()