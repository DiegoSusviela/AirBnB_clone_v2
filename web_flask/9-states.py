#!/usr/bin/python3
"""starts flask"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """returns"""
    state_dict = storage.all(State)
    if id:
        return render_template('9-states.html', state=state, id=id)


@app.teardown_appcontext
def teardown_db(self):
    """returns"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
