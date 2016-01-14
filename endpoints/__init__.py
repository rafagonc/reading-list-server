__author__ = 'rafagonc'
from .rating import RatingBookRequest
from flask import Blueprint
from .api import api

def create_blueprint():
    api.init_app(blueprint)
    api.add_resource(RatingBookRequest, '/rating')

blueprint = Blueprint('endpoints', __name__)
create_blueprint()