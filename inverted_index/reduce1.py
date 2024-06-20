#!/usr/bin/env python3
"""Reduce 1."""

import sys

# input is {doc_id}\t{content}
for line in sys.stdin:
    line = line.strip()
    print(line)
