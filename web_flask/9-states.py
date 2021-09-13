#!/usr/bin/python3
"""starts flask"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
def states():
    """returns"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def remove_sesh(self):
    """returns"""
    storage.close()

@app.route("/states/<id>")
def statesId(id=None):
    """returns"""
    aux = storage.all(State)
    check = False
    states = None
    for s in aux.values():
        if s.id == id:
            states = s
            check = True
            break
    return render_template('9-states.html', states=states, check=check)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
