#!/usr/bin/python3
"""
This module starts a Flask web app listening on 0.0.0.0:5000.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Returns a welcome string"""

    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns HBNB"""

    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Displays "C " followed by the value of the text variable"""

    updated_text = text.replace('_', ' ')
    return 'C ' + updated_text


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is cool'):
    """Displays "Python " followed by the value of the text variable"""

    updated_text = text.replace('_', ' ')
    return 'Python ' + updated_text


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """Displays "n is a number" if n is an integer"""

    if isinstance(int(n), int):
        return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def is_number_template(n):
    """Displays an HTML page if n is an integer"""

    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def is_even_odd(n):
    """Displays an HTML page if n is an integer"""

    if n % 2 == 0:
        even_odd = 'even'
    else:
        even_odd = 'odd'

    return render_template('6-number_odd_or_even.html', n=n, even_odd=even_odd)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
