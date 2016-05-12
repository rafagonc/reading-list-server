from flask_restful import Resource, reqparse
from schemas.book import BookSchema
from dao.user import user_by_id
from db import db
from models.book import Book
from models.user_books import UserBooks
from schemas.user_book import UserBookSchema
from dao import book as dao
from validator.book import validate
from dao.user import user_by_user_id
from general.response import simple_response
from dao.user_book import  user_book_from_book_id, user_book_from_book_name, list_user_books
import json

parser = reqparse.RequestParser()

class BookEndpoint(Resource):
    """

    Controls the CRUD of the book model.

    @see Book

    """
    def post(self):
        return append_book()

    def delete(self):
        return delete_book()

    def put(self):
        return update_book()

    def get(self):
        return list_books()


def append_book():
    """
    Appends an array of books to the user. But,
    it doesnt change any of the book metadata, just
    append a new book by having a m:n table between
    user and book.

    @return JSON with success and message

    @see User, UserBooks, Book

    """
    parser.add_argument("books", type=dict, action='append')
    parser.add_argument("user_id", type=int, required=False)
    args = parser.parse_args()
    return append_book_impl(args)


def append_book_impl(args):
    try:
        user = user_by_user_id(args['user_id'])
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


def delete_book():
    """
    Removes an book from the user. Deletes
    info like pages, paged_read, snippet, and rate.

    @return JSON with success and message

    @see User, UserBooks, Book

    """
    parser.add_argument("user_id", type=int)
    parser.add_argument("book_name", type=str)
    args = parser.parse_args()
    return delete_book_impl(args)

def delete_book_impl(args):
    try:
        book = user_book_from_book_name(args['book_name'], user_by_id(args['user_id']).id)
        db.session.delete(book)
        db.session.commit()
        return json.dumps(simple_response(True, "Book Deleted"))
    except Exception as e:
        return json.dumps(simple_response(False, str(e)))


def update_book():
    """

    Update an instance of UserBook from the info
    of an user and a book id. It can only update pages,
    pages_read, snippet (that may not change) and rate.

    @see UserBooks

    """
    parser.add_argument("book_id", type=int)
    parser.add_argument("user_id", type=int)
    parser.add_argument("pages", type=int, required=False)
    parser.add_argument("pages_read", type=int, required=False)
    parser.add_argument("snippet", type=str, required=False)
    parser.add_argument("rate", type=float, required=False)
    args = parser.parse_args()
    return update_book_impl(args)


def update_book_impl(args):
    try:
        book = user_book_from_book_id(args['book_id'], user_by_id(args['user_id']).id)
        book.pages = args['pages'] if args.has_key('pages') else book.pages
        book.pages_read = args['pages_read'] if args.has_key('pages_read') else book.pages_read
        book.snippet = args['snippet'] if args.has_key('snippet') else book.snippet
        book.rate = args['rate'] if args.has_key('rate') else book.rate
        db.session.commit()
        return json.dumps(simple_response(True, "Book Updated"))
    except Exception as e:
        return json.dumps(simple_response(False, str(e)))


def list_books():
    """

    Fetch the user entire user book list.

    @see Book

    """
    parser.add_argument("user_id", type=int,)
    args = parser.parse_args()
    return list_books_impl(args)


def list_books_impl(args):
    try:
        user_books = list_user_books(args['user_id'])
        return json.loads(UserBookSchema(many=True).dumps(user_books).data)
    except Exception as e:
        return json.dumps(simple_response(False, str(e)))


class TopRatedBooksRequest(Resource):
    """

    Fetch top rated books from the anonymous rating given by users
    (Using the red_rating table)

    @see Rating

    """
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