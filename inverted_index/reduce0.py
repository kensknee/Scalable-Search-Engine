#!/usr/bin/env python3
"""Reduce 0."""

import sys
total_count = 0
for line in sys.stdin:
    key, value = line.strip().split("\t", 1)
    if key == "document":
        # Shouldn't ever be false anyways
        total_count += int(value)

print(total_count)