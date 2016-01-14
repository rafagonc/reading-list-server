from flask_restful import Resource, reqparse
from db import db
from schemas.book import BookSchema
from models.rating import Rating
from models.book import Book
from dao.book import find_book_with_name
from red_exceptions import InvalidBookNameException, InvalidRatingException
import json

parser = reqparse.RequestParser()
parser.add_argument("book_name", type=str, required=True)
parser.add_argument("author_name", type=str, required=True)
parser.add_argument("category_name", type=str, required=True)
parser.add_argument("rating", type=float, required=True)


class RatingBookRequest(Resource):
    def post(self):
        return rating_book_request()

def rating_book_request():
    args = parser.parse_args()
    return rating_book_request_impl(args)


def rating_book_request_impl(args):
    try:
        book_name = args['book_name']
        author_name = args['author_name']
        category_name = args['category_name']
        rating = args['rating']

        if len(book_name) == 0:
            raise InvalidBookNameException

        if rating < 0 or rating > 5:
            raise InvalidRatingException

        book = find_book_with_name(book_name)
        if book is None:
            print author_name
            book = Book(book_name, author_name, category_name)
            db.session.add(book)

        rating = Rating(rating, book)
        db.session.add(rating)

        book.ratings.append(rating)
        db.session.commit()

        return BookSchema().dumps(book).data
    except Exception as e:
        return json.dumps({"error": str(e)})
