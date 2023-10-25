#!/usr/bin/python3
'''
This script is a training on flask in python
'''
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)


@app.teardown_appcontext
def close_conn(exc):
    """
    remove the current SQLAlchemy Session
    """
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def states():
    '''
    display the hbnb_filters page,
    manipulate the static html to allow for scroll down when
    selecting states and amenities
    '''
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html',
                           states=states,
                           amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
