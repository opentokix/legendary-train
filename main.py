#!/usr/bin/env python2
"""A simple flask app."""

from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    """Root function."""
    return "Hello World!"

if __name__ == '__main__':
    app.run()
