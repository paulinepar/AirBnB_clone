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
    states = storage.all(State)

    if states:
        states_list = sorted(states.values(), key=lambda x: x.name)
    else:
        states_list = []
    return render_template('7-states_list.html', states=states_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
