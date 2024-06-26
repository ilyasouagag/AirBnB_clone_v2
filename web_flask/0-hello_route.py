#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display():
    """display hello hbnb in the root"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
