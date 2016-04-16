__author__ = 'rafagonc'
from .rating import RatingBookRequest
from .book import  TopRatedBooksRequest
from flask import Blueprint
from .api import api

def create_blueprint():
    api.init_app(blueprint)
    api.add_resource(RatingBookRequest, '/rating')
    api.add_resource(TopRatedBooksRequest, '/book/top')

blueprint = Blueprint('endpoints', __name__)
create_blueprint()