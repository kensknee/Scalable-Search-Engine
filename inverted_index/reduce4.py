#!/usr/bin/env python3
"""Reduce 4."""
import sys
import itertools
import math
# Goal in this job: get normalization factor
# Need to loop through k terms and i documents
def reduce_one_group(key, document):
    """Reduce one group."""
    # input: term, tf_ik, doc_id, w_ik

    #print(key) # DEBUG
    # Loop through i documents of k terms
    summation = 0
    info = []

    for word_info in document:
        doc_id, term, tf_ik, idf_k, w_ik = word_info.strip().split("\t", 4)
        info.append((doc_id, term, tf_ik, idf_k))
        # Summation across all terms in a document(items)
        summation += float(w_ik)**2
    # Normalization factor of 
    normalization_factor = summation
    #print(info)
    for item in info:


        print(f"{item[1]}\t{item[3]}\t{item[0]}\t{item[2]}\t{normalization_factor}")
        # term, idf_k, doc_id, tf_ik, normalization factor

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


