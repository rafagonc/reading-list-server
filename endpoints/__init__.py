__author__ = 'rafagonc'
from .rating import RatingBookRequest
from .book import  TopRatedBooksRequest
from .rating import MultipleRatingBookRequest
from .book import BookEndpoint
from .log import LogEndpoint
from .user import UserEndpoint
from flask import Blueprint
from .api import api

def create_blueprint():
    api.init_app(blueprint)
    api.add_resource(RatingBookRequest, '/rating')
    api.add_resource(MultipleRatingBookRequest, '/mrating')
    api.add_resource(TopRatedBooksRequest, '/book/top')
    api.add_resource(BookEndpoint, '/book')
    api.add_resource(LogEndpoint, '/log')
    api.add_resource(UserEndpoint, '/user')


blueprint = Blueprint('endpoints', __name__)
create_blueprint()