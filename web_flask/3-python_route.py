#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display():
    """display hello hbnb in the root"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    "display HBNB in /hbnb"
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def message(text):
    "display text message in /c/<text>"
    return "C {}".format(text.replace('_', ' '))

@app.route("/python", strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    "display text message in python/<text>"
    return "Python {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
