#!/usr/bin/python3
# First you have to import Flask class.
from flask import Flask

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


@app.route('/hbnb', strict_slashes=False)
def hbnb_flask():
    """
    Defines other route - Routing -
    """
    return 'HBNB'


if __name__ == '__main__':
    # Call run method of our instance, and defines host and port
    app.run(host="0.0.0.0", port=5000)
