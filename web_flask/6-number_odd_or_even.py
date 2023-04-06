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


@app.route("/python/", defaults={'text': "is cool"})
@app.route("/python/<text>", strict_slashes=False)
def index3(text):
    ''''display Python followed by the value of the text'''
    return "Python " + text.replace('_', ' ')


@app.route("/number/<int:n>")
def index4(n):
    '''display n is a number just if is integer'''
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def index5(n):
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
