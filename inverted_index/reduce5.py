#!/usr/bin/env python3
"""Reduce 5."""
import sys
import itertools


# Goal in this job: get normalization factor
# Need to loop through k terms and i documents
def reduce_one_group(document):
    """Reduce one group."""
    for word_info in document:
        term, idf_k, doc_id, tf_ik, norm = word_info.strip().split("\t", 4)
        print(f"{term}\t{idf_k}\t{doc_id}\t{tf_ik}\t{norm}")


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]


def main():
    """Divide sorted lines into groups that share a key and reduce."""
    for _, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(group)
        # key is term


if __name__ == "__main__":
    main()
