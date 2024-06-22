#!/usr/bin/env python3
"""Map 0"""

import csv
import sys

"""
Job 0
The first MapReduce job counts the total number of documents in the collection.
It should read input from crawl/ and write output to output0/.

The mapper and reducer executables should be named map0.py and reduce0.py.
The output should be a single integer. Hint: each HTML document contains
exactly one <!DOCTYPE html> tag.

In pipeline.sh, copy the output (e.g., output0/part-00000) to
total_document_count.txt.

In later pipeline jobs, read the document count from 
total_document_count.txt, not output0/part-00000.
"""

# Works
csv.field_size_limit(sys.maxsize)
for line in sys.stdin:
    if '<!DOCTYPE html>' in line:
        print(f"document\t1") # This is the key value pair that will be passed to the reducer