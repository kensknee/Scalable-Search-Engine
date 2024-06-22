#!/usr/bin/env python3
"""Reduce 2."""
import sys
import itertools
# Cleaning and Proprocessing Stage


def reduce_one_group(key, group):
    """Reduce one group."""
    # Input: {term}\t{doc_id}
    # Output: {term}\t{doc_id:count}
    doc_count = {}
    for line in group:
        term, doc_id = line.strip().split("\t", 1)
        doc_count[doc_id] = doc_count.get(doc_id, 0) + 1
    # key is term
    for doc_id, frequency in doc_count.items():
        print(f"{key}\t{doc_id}\t{frequency}")
        # term k, document i, frequency of term t_k in document d_i

def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]

def main():
    # input is {term}\t{doc_id} --- a lot of rows!
    """Divide sorted lines into groups that share a key and reduce."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        # Groups values by key (term)
        reduce_one_group(key, group)

if __name__ == "__main__":
    main()


