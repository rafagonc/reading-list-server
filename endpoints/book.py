from flask_restful import Resource, reqparse
from schemas.book import BookSchema
from db import db
from models.book import Book
from models.user_books import UserBooks
from dao import book as dao
from validator.book import validate
from dao.user import user_by_id
from general.response import simple_response
import json

parser = reqparse.RequestParser()
parser.add_argument("books", type=dict, action='append')
parser.add_argument("user_id", type=int, required=False)

class BookEndpoint(Resource):
    def post(self):
        return append_book()


def append_book():
    args =parser.parse_args()
    return append_book_impl(args)


def append_book_impl(args):
    try:
        user = user_by_id(args['user_id'])
        for book_dict in args['books']:
            validate(book_dict)
            book_name = book_dict['name']
            book = dao.find_book_with_name(book_name)
            if book is None:
                book = Book(book_name, book_dict['author'], book_dict['category'])
            user_book = UserBooks(user, book,  book_dict['pages_read'],  book_dict['pages'], book_dict['rate'], book_dict["snippet"])
            db.session.add(user_book)
            db.session.commit()
        return json.dumps(simple_response(True, "Book Updated/Created"))
    except Exception as e:
        return json.dumps(simple_response(False, str(e)))


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