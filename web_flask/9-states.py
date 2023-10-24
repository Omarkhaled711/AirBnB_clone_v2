#!/usr/bin/python3
'''
This script is a training on flask in python
'''
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def close_conn(exc):
    """
    remove the current SQLAlchemy Session
    """
    storage.close()


@app.route("/states", strict_slashes=False)
def states(id=None):
    '''
    display states in html page
    '''
    states = storage.all(State).values()
    return render_template('9-states.html', states=states, id=id)


@app.route("/states/<id>", strict_slashes=False)
def state_cities(id):
    '''
    display states and cities in html page
    '''
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            return render_template('9-states.html',
                                   state=state, id=id)
    return render_template('9-states.html', id=id, state=None)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
