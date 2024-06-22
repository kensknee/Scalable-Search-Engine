#!/usr/bin/env python3
"""Map 0."""

import csv
import sys


# Works
csv.field_size_limit(sys.maxsize)
for line in sys.stdin:
    if '<!DOCTYPE html>' in line:
        print("document\t1")
