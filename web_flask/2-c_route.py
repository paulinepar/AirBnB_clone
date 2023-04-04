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


@app.route("/c/<text>")
def index2(text=None):
    return render_template("C.html", C=text)


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
