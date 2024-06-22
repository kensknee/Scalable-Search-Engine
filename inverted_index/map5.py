#!/usr/bin/env python3
"""Map 5"""
import sys
import math

# calculate IDF - Inverse Document Frequency
# IDF(t) = log(N/df(t))
# N = total number of documents
# df(t) = number of documents containing the term t
# Input: term k, document i, number of times that term k appears in document i

# Goal in this job: Print final result
# term, idf_k, doc_id, tf_ik, normalization factor
for line in sys.stdin:
    term, idf_k, doc_id, tf_ik, norm = line.strip().split("\t", 4)
    print(f"{term}\t{idf_k}\t{doc_id}\t{tf_ik}\t{norm}")
