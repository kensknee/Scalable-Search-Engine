"""Initializer for the search package."""

import flask
from search import config

app = flask.Flask(__name__)
app.config.from_object(config)

import search.views.index
import search.model