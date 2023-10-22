#!/usr/bin/python3
'''
This script is a start file with flask in python
'''
from flask import Flask, render_template

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


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    '''
    display "C" followed by the value of the text variable
    '''
    return f'C {text.replace("_", " ")}'


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def py_text(text='is cool'):
    '''
    display "Python" followed by the value of the text variable
    '''
    return f'Python {text.replace("_", " ")}'


@app.route("/number/<int:n>", strict_slashes=False)
def show_number(n):
    '''
    display an integer number
    '''
    return f'{n} is a number'


@app.route("/number_template/<int:n>", strict_slashes=False)
def html_number(n):
    '''
    display an integer number in an html page
    '''
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
