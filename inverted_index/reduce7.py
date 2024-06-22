#!/usr/bin/env python3
"""Reduce 7."""
import sys
import itertools
import math
# Goal in this job: get normalization factor
# Need to loop through k terms and i documents
def reduce_one_group(key, group):
    """Reduce one group."""
    #print(f"key: {key}")
    #{doc_id}\t{term}\t{tf_ik}\t{idf_k}\t{norm}
    term = key[0]
    idf = key[1]
    output = [term, idf]
    # print(f"{term}\t{idf}")
    for item in group:
        # term, idf, doc_id, tf, norm
        term2, idf2, doc_id, tf, norm = item.strip().split("\t", 4)
        if term == term2 and idf == idf2:
            #print(f"{doc_id}\t{tf}\t{norm}")
            output.append(doc_id)
            output.append(tf)
            output.append(norm)

        #print(f"{term}\t{idf}\t{doc_id}\t{tf}\t{norm}")
    #print(f"output: {output}")
    print(" ".join(output))


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0], line.split('\t')[1]


def main():
    """Divide sorted lines into groups that share a key and reduce."""
    # one rep for every term
    # "{doc_id}\t{term}\t{tf_ik}\t{idf_k}\t{norm}")
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)


if __name__ == "__main__":
    main()







