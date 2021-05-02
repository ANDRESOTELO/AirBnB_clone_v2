#!/usr/bin/python3
"""
Comment
"""

from flask import Flask
from models import storage
from models.state import State
from flask import render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    """
    Method to render a template
    """
    state_dictionary = storage.all(State)
    states = {}
    for key, value in state_dictionary.items():
        states[value.id] = value.name
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def tear_down(self):
    """
    Method to remove the current SQLAlchemy Session
    """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
