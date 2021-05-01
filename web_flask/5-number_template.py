#!/usr/bin/python3
# First you have to import Flask class.
"""
script that starts a Flask web application
"""
from flask import Flask
# To render a template you can use the render_template() method
from flask import render_template

# An instance of Flask class, it will be our application
# First argument is the name of the package or module
app = Flask(__name__)


# decorator is used to tell Flask what URL should trigger our function
@app.route('/', strict_slashes=False)
def hello_flask():
    """
    Function to stars a Flask web application and return a message
    """
    return 'Hello HBNB!'


# Routing
@app.route('/hbnb', strict_slashes=False)
def hbnb_flask():
    """
    Defines other route - Routing -
    """
    return 'HBNB'


# Variable routes
@app.route('/c/<text>', strict_slashes=False)
def variable_routes(text):
    """
    You can add variable sections to a URL by marking sections with
    <variable_name>. Your function then receives the <variable_name>
    as a keyword argument
    """
    text = text.replace('_', ' ')
    return ('C {}'.format(text))


# Other routes
# stackoverflow.com/questions/14032066/can-flask-have-optional-url-parameters
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def other_routes(text):
    """
    Other vairable route
    """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


# Display a number only if is an integer
@app.route('/number/<int:n>')
def is_integer(n):
    """
    Diplay a number n only if the number is an integer
    """
    return '{} is a number'.format(n)


# Route to rendering a template
@app.route('/number_template/<int:n>')
def redering_template(n):
    """
    To render a template you can use the render_template() method.
    All you have to do is provide the name of the template and the
    variables you want to pass to the template engine as keyword
    arguments.
    """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    # Call run method of our instance, and defines host and port
    app.run(host="0.0.0.0", port=5000)
