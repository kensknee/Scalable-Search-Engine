#!/usr/bin/env python3
"""Map 3"""
import sys
import math

# calculate IDF - Inverse Document Frequency
# IDF(t) = log(N/df(t))
# N = total number of documents
# df(t) = number of documents containing the term t
# Input: term k, document i, number of times that term k appears in document i

# Goal in this job: get IDF for every term in every document
previous_term = None
for line in sys.stdin:
    term, doc_id, frequency = line.strip().split("\t", 2)
    print(f"{term}\t{doc_id}\t{frequency}")
