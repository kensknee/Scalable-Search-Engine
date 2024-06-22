#!/usr/bin/env python3
"""Reduce 3."""
import sys
import itertools
import math


def get_tfidf(tf, idf):
    """Calculate w_ik = tf_ik * idf_k."""
    return tf * idf


def reduce_one_group(key, group):
    """Reduce one group."""
    with open('total_document_count.txt', 'r', encoding="utf-8") as f:
        total_docs = int(f.read().strip())

    group = list(group)

    # term is key
    idf_k = math.log10(total_docs / len(group))

    for item in group:
        # print(f"Term Info: {item.strip().split("\t")}") # DEBUG
        # print(f"Doc ID: {item.strip().split("\t")[1]}") # DEBUG
        # print(f"Term Freq in Doc: {item.strip().split("\t")[2]}") # DEBUG

        # d_i
        doc_id = item.strip().split("\t")[1]
        # tf_ik
        tf_ik = int(item.strip().split("\t")[2])

        # output.append(f"{doc_id}")
        # output.append(f"{tf_ik}")
        print(f"{key.strip()}\t{doc_id}" +
              f"\t{tf_ik}\t{idf_k}\t{get_tfidf(tf_ik, idf_k)}")
    # print("\t".join(output))


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]


def main():
    """Divide sorted lines into groups that share a key and reduce."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)
        # key is term


if __name__ == "__main__":
    main()
