#!/usr/bin/python
"""This module defines the index"""

from . import app_views
from flask import jsonify
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.city import City
from models.review import Review
from models.user import User
from models import storage

CLASSES = {
    'amenities': Amenity,
    'states': State,
    'places': Place,
    'cities': City,
    'reviews': Review,
    'users': User
}


@app_views.route('/status')
def status():
    """
    Method that returns a Json with an Ok status
    """

    return jsonify({'status': 'OK'})


@app_views.route('/stats')
def stats():
    """
    Method that retrieves the number of each objects by type
    """

    stats = {}
    for key, value in CLASSES.items():
        stats[key] = storage.count(value)
    return jsonify(stats)
