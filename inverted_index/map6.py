#!/usr/bin/env python3
"""Map 6."""
import sys


# input: term, idf, doc_id, tf, norm
for line in sys.stdin:
    term, idf_k, doc_id, tf_ik, norm = line.strip().split("\t", 4)
    print(f"{idf_k}\t{term}\t{doc_id}\t{tf_ik}\t{norm}")
