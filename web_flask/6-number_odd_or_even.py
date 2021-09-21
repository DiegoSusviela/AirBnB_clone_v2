#!/usr/bin/python3
"""starts flask"""

from flask import Flask, abort, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """returns"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cfun(text):
    """returns"""
    return 'C %s' % text.replace("_", " ")


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoncool(text='is cool'):
    """returns"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<n>', strict_slashes=False)
def numver(n):
    """returns"""
    try:
        return '%d is a number'.format(int(n))
    except:
        abort(404)


@app.route('/number_template/<n>', strict_slashes=False)
def number_templates(n):
    """returns"""
    try:
        return render_template('5-number.html', n=int(n))
    except:
        abort(404)


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def numbersandevenness(n):
    """display a HTML page only if n is an integer"""
    try:
        return render_template('6-number_odd_or_even.html', n=int(n))
    except:
        abort(404)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
