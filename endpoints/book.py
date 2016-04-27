from flask_restful import Resource, reqparse
from schemas.book import BookSchema
from dao import book as dao
from general.response import simple_response
import json

parser = reqparse.RequestParser()
parser.add_argument("books", type=dict, action='append')

class BookEndpoint(Resource):
    def post(self):
        return append_book()


def append_book():
    args =parser.parse_args()
    return append_book_impl(args)


def append_book_impl(args):
    try:
        for book_dict in args['books']:
            book_name = book_dict['name']
            book = dao.find_book_with_name(book_name)
            if book is None:

        return simple_response(True, "Book Updated/Created")
    except Exception as e:
        return simple_response(False, str(e))




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