# This file is required to make Python treat the directory as a package.
from flask import Flask, jsonify, request
from .. import stopwords, inverted_index, pagerank, app


def compute_hits(query, weight=0.5):
    query_terms = query.split()
    query_terms = [term for term in query_terms if term not in stopwords]

    if not query_terms:
        return []

    docid_scores = {}
    docid_sets = []

    for term in query_terms:
        if term in inverted_index:
            postings = inverted_index[term]
            docids_for_term = set()
            for i in range(1, len(postings), 3):
                docid = int(postings[i])
                score = float(postings[i + 2])
                if docid not in docid_scores:
                    docid_scores[docid] = 0.0
                docid_scores[docid] += weight * score
                docids_for_term.add(docid)
            docid_sets.append(docids_for_term)
        else:
            return []

    common_docids = set.intersection(*docid_sets)
    filtered_docid_scores = {docid: docid_scores[docid] for docid in common_docids}

    sorted_hits = sorted(filtered_docid_scores.items(), key=lambda item: pagerank.get(item[0], 0), reverse=True)

    hits = [{"docid": docid, "score": score} for docid, score in sorted_hits]

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