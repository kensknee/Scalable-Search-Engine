from pathlib import Path
from flask import Flask
import os

import index.api  # noqa: E402  pylint: disable=wrong-import-position

# Load inverted index, stopwords, and pagerank into memory
#index.api.load_index()
app = Flask(__name__)
print("+++INIT+++")

# Configure INDEX_PATH from the environment variable
app.config["INDEX_PATH"] = os.getenv("INDEX_PATH", "inverted_index_1.txt")

# Base directory is the directory where this script is located
BASE_DIR = Path(__file__).resolve().parent

# Paths to the necessary files
STOPWORDS_FILE = BASE_DIR / 'stopwords.txt'
INVERTED_INDEX_FILE = BASE_DIR / 'inverted_index' / app.config["INDEX_PATH"]
PAGERANK_FILE = BASE_DIR / 'pagerank.out'

def load_stopwords():
    with STOPWORDS_FILE.open('r') as file:
        stopwords = set(file.read().splitlines())
    return stopwords

def load_inverted_index():
    inverted_index = {}
    with INVERTED_INDEX_FILE.open('r') as file:
        for line in file:
            parts = line.split()
            term = parts[0]
            postings = parts[1:]
            inverted_index[term] = postings
    return inverted_index

def load_pagerank():
    pagerank = {}
    with PAGERANK_FILE.open('r') as file:
        for line in file:
            docid, rank = line.split(',')
            pagerank[int(docid)] = float(rank)
    return pagerank

stopwords = load_stopwords()
inverted_index = load_inverted_index()
pagerank = load_pagerank()
