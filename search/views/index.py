"""Index handler for P5 Search."""
import flask
import requests
import threading
import heapq

from search import app, model


@app.route('/', methods=['GET'])
def index():
    """Main search page."""
    query = flask.request.args.get('q', '')
    weight = flask.request.args.get('w', 0.5, type=float)

    print(f"Received query: {query}, weight: {weight}")

    api_urls = app.config['SEARCH_INDEX_SEGMENT_API_URLS']
    results = []

    def fetch_results(url):
        try:
            response = requests.get(url, params={'q': query, 'w': weight})
            response.raise_for_status() 
            data = response.json()
            if data:
                hits = data.get('hits', [])
                print(f"Fetched from {url}: {hits}")
                results.extend(hits)
            else:
                print(f"No data returned from {url}")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching results from {url}: {e}")
        except ValueError as e:
            print(f"Error parsing JSON response from {url}: {e}")

    # handle threading here dont forgot to close
    threads = []
    for url in api_urls:
        thread = threading.Thread(target=fetch_results, args=(url,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    # Debugging
    print("Results fetched from index servers:", results)

    # Ensure the results are dictionaries with 'docid' and 'score'
    if results and all(isinstance(result, dict) for result in results):
        # Merge results from index servers
        merged_results = heapq.nlargest(10, results, key=lambda x: x['score'])
    else:
        merged_results = []

    # Debugging
    print("Merged results:", merged_results)

    # Query db for doc details
    db = model.get_db()
    doc_details = []
    for result in merged_results:
        docid = result.get('docid')
        if docid is not None:
            a = 'SELECT title, summary, url FROM documents WHERE docid = ?'
            doc = db.execute(a, (docid,)).fetchone()
            if doc:
                doc_details.append({
                    "docid": docid,
                    "title": doc['title'],
                    "summary": doc['summary'],
                    "url": doc['url'],
                    "score": result['score']
                })

    # Debugging
    print("Document details:", doc_details)

    return flask.render_template('index.html', query=query, weight=weight, results=doc_details)
