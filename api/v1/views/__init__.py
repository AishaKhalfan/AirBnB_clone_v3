#!/usr/bin/python3
<<<<<<< HEAD
"""file for views module"""
=======

"""init file for views module"""

>>>>>>> origin/storage_get_count
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
