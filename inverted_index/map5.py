#!/usr/bin/env python3
"""Map 5."""
import sys


for line in sys.stdin:
    term, idf_k, doc_id, tf_ik, norm = line.strip().split("\t", 4)
    print(f"{term}\t{idf_k}\t{doc_id}\t{tf_ik}\t{norm}")
