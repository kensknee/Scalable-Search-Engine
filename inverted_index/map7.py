#!/usr/bin/env python3
"""Map 7."""
import sys


# input: term, idf, doc_id, tf, norm
for line in sys.stdin:
    term, idf_k, doc_id, tf_ik, norm = line.strip().split("\t", 4)
    # doc_mod = int(doc_id) % 3
    doc_mod = doc_id
    print(f"{term}\t{idf_k}\t{doc_id}\t{tf_ik}\t{norm}")
    # print(f"{doc_id}\t{term}\t{tf_ik}\t{idf_k}\t{norm}")
    # print(f"{doc_mod}\t{term}\t{idf_k}\t{doc_id}\t{tf_ik}\t{norm}")
