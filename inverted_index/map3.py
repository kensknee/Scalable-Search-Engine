#!/usr/bin/env python3
"""Map 3."""
import sys


# Goal in this job: get IDF for every term in every document
for line in sys.stdin:
    term, doc_id, frequency = line.strip().split("\t", 2)
    print(f"{term}\t{doc_id}\t{frequency}")
