#!/usr/bin/python3
'''Before using Flask to display our HBNB data,
you will need to update some part of our engine
'''


from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """ After each request remove the current SQLAlchemy """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ display a HTML page"""
    print(storage.all("State"))
    return render_template('7-states_list.html',
                           states=storage.all("State"))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')