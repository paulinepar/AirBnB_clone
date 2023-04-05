#!/usr/bin/python3
'''script that starts a Flask web application'''
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def index_1():
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def index2(text):
    '''display 'C ' followed by the value of the text variable'''
    return "C " + text.replace('_', ' ')


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def index3(text="is cool"):
    ''''display Python followed by the value of the text'''
    return "Python" + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
