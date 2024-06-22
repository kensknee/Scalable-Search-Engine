#!/usr/bin/env python3
"""Map 2"""
import sys
import re
# Cleaning and Preprocessing Stage

# Input: {doc_id}\t{content}
stopwords = set()
with open("stopwords.txt", 'r') as stopfile:
    for stopword in stopfile:
        stopwords.add(stopword.strip())

for line in sys.stdin:
    doc_id, content = line.strip().split("\t", 1)
    cleaned = re.sub(r"[^a-zA-Z0-9]", " ", content)

    cleaned = cleaned.casefold()
    # print(f"cleaned: {cleaned}")
    terms = cleaned.split()
    # print(f"terms: {terms}")
    cleaned_terms = [term for term in terms if term not in stopwords]
    for term in cleaned_terms:
        print(f"{term}\t{doc_id}")