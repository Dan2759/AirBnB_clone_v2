#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)

@app.route('/hbnb', strict_slashes=False)
def filters():
    """Display the main HBNB filters HTML pages."""
    states = storage.all("State")

    amenities = storage.all("Amenity")

    place = storage.all("Place")
    return render_template('100-hbnb.py', states=states,
                           amenities=amenities, places=places)

@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy session."""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
