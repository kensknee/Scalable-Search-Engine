#!/usr/bin/env python3
"""Reduce 3."""
import sys
import itertools
import math
# Cleaning and Proprocessing Stage

# calculate IDF - Inverse Document Frequency
# IDF(t) = log(N/df(t))
# N = total number of documents : TOTAL_DOCS
# df(t) = number of documents containing the term t : len(group)
# Input: term k, document i, number of times that term k appears in document i

# Goal in this job: get IDF for every term in every document
def get_tfidf(tf, idf):
    """Calculate w_ik = tf_ik * idf_k"""
    return tf * idf


def reduce_one_group(key, group):
    """Reduce one group."""
    with open('total_document_count.txt', 'r') as f:
        TOTAL_DOCS = int(f.read().strip())

    group = list(group)

    """NON-LOOPED STUFF:"""
    # term is key
    idf_k = math.log10(TOTAL_DOCS / len(group))

    """LOOPED STUFF:"""
    for item in group:
        """Looped part needs: document_id, term_frequency_in_doc, normalization factor"""
        #print(f"Term Info: {item.strip().split("\t")}") # DEBUG
        #print(f"Doc ID: {item.strip().split("\t")[1]}") # DEBUG
        #print(f"Term Freq in Doc: {item.strip().split("\t")[2]}") # DEBUG

        # d_i
        doc_id = item.strip().split("\t")[1]
        # tf_ik
        tf_ik = int(item.strip().split("\t")[2])

        #output.append(f"{doc_id}")
        #output.append(f"{tf_ik}")
        print(f"{key.strip()}\t{doc_id}\t{tf_ik}\t{idf_k}\t{get_tfidf(tf_ik, idf_k)}")
    #print("\t".join(output))


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]

def main():
    """Divide sorted lines into groups that share a key and reduce."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)
        # key is term

if __name__ == "__main__":
    main()


