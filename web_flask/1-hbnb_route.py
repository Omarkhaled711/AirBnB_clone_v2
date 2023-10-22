#!/usr/bin/python3
'''
This script is a start file with flask in python
'''
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    '''
    A trial method to start with flask
    '''
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    '''
    A method that shows HBNB with the /hbnb route
    '''
    return 'HBNB'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
