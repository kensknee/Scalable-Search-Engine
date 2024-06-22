#!/usr/bin/env python3
"""Reduce 6."""
import sys
import itertools


# Goal in this job: get normalization factor
# Need to loop through k terms and i documents
def reduce_one_group(group):
    """Reduce one group."""
    for line in group:
        idf, term, doc_id, tf, norm = line.strip().split("\t", 4)
        print(f"{term}\t{idf}\t{doc_id}\t{tf}\t{norm}")


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]


def main():
    """Divide sorted lines into groups that share a key and reduce."""
    for _, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(group)
        # key is idf


if __name__ == "__main__":
    main()
