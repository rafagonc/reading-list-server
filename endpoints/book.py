from flask_restful import Resource, reqparse
from schemas.book import BookSchema
from dao import book as dao
import json

parser = reqparse.RequestParser()

class TopRatedBooksRequest(Resource):
    def get(self):
        return top_rated_books()


def top_rated_books():
    args = parser.parse_args()
    return top_rated_books_impl(args)


def top_rated_books_impl(args):
    try:
        books = dao.top_rated_books()
        return json.loads(BookSchema(many=True).dumps(books).data)
    except Exception as e:
        return json.dumps({"error": str(e)})