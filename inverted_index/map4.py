#!/usr/bin/env python3
"""Map 4"""
import sys
import math

# calculate IDF - Inverse Document Frequency
# IDF(t) = log(N/df(t))
# N = total number of documents
# df(t) = number of documents containing the term t
# Input: term k, document i, number of times that term k appears in document i

# Goal in this job: Normalization factor
# input: (term) \t (doc_id) \t (tf_ik) \t (tf-idf)
for line in sys.stdin:
    term, doc_id, tf_ik, idf_k, w_ik = line.strip().split("\t", 4)
    #key_pair = (term, tf_ik) # tuple
    print(f"{doc_id}\t{term}\t{tf_ik}\t{idf_k}\t{w_ik}")
