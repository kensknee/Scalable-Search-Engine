# This file is required to make Python treat the directory as a package.
from flask import Flask, jsonify, request
from .. import stopwords, inverted_index, pagerank, app

import math

def compute_hits(query, weight=0.5):
    query_terms = query.split()
    query_terms = [term for term in query_terms if term not in stopwords]

    if not query_terms:
        return []

    # Compute the query vector
    query_vector = {}
    for term in query_terms:
        if term in query_vector:
            query_vector[term] += 1
        else:
            query_vector[term] = 1

    for term in query_vector:
        if term in inverted_index:
            postings = inverted_index[term]
            idf = float(postings[0])
            query_vector[term] *= idf

    # Compute the norm of the query vector
    query_norm = math.sqrt(sum(value ** 2 for value in query_vector.values()))

    docid_scores = {}
    docid_sets = []

    for term in query_terms:
        if term in inverted_index:
            postings = inverted_index[term]
            docids_for_term = set()
            for i in range(1, len(postings), 3):
                docid = int(postings[i])
                term_frequency = float(postings[i + 1])
                idf = float(postings[0])
                doc_norm = float(postings[i + 2])
                doc_vector_entry = term_frequency * idf
                if docid not in docid_scores:
                    print(docid)
                    docid_scores[docid] = {
                        'tfidf': 0.0,
                        'norm': doc_norm
                    }
                docid_scores[docid]['tfidf'] += query_vector[term] * doc_vector_entry
                docids_for_term.add(docid)
            docid_sets.append(docids_for_term)
        else:
            return []
    common_docids = set.intersection(*docid_sets)

    # Calculate the final score for each document
    for docid in common_docids:
        if query_norm != 0 and docid_scores[docid]['norm'] != 0:
            tfidf_score = docid_scores[docid]['tfidf'] / (query_norm * docid_scores[docid]['norm'])
        else:
            tfidf_score = 0.0
        pagerank_score = pagerank.get(docid, 0)
        print(pagerank_score)
        final_score = weight * pagerank_score + (1 - weight) * tfidf_score
        docid_scores[docid] = final_score

    # Sort the documents by final score
    sorted_hits = sorted(common_docids, key=lambda docid: docid_scores[docid], reverse=True)

    hits = [{"docid": docid, "score": docid_scores[docid]} for docid in sorted_hits]

    return hits


@app.route('/api/v1/', methods=['GET'])
def index():
    return jsonify({
        "hits": "/api/v1/hits/",
        "url": "/api/v1/"
    })

@app.route('/api/v1/hits/', methods=['GET'])
def get_hits():
    query = request.args.get('q', '')
    weight = float(request.args.get('w', 0.5))

    if not query:
        return jsonify({"error": "Missing query parameter 'q'"}), 400

    hits = compute_hits(query, weight)

    return jsonify({"hits": hits})

if __name__ == '__main__':
    app.run(debug=True)