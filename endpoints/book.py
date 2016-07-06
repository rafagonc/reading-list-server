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
from dao.user_book import  user_book_from_book_id, user_book_from_book_name, list_user_books
from response import Response
import json


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
    parser = reqparse.RequestParser()
    parser.add_argument("books", type=dict, action='append')
    parser.add_argument("user_id", type=str, required=False)
    args = parser.parse_args()
    return append_book_impl(args)


def append_book_impl(args):

    try:
        user = user_by_user_id(args['user_id'])
        books = []
        if args['books'] is None:
            return Response(True, "Books Appended", UserBookSchema(many=True).dumps(books).data).output()
        for book_dict in args['books']:
            validate(book_dict)
            book_name = book_dict['name']
            book = dao.find_book_with_name(book_name)
            if book is None:
                book = Book(book_name, book_dict['author'], book_dict['category'])
                db.session.add(book)
                db.session.commit()
            try:
                user_book = user_book_from_book_name(book_name, user_by_user_id(args['user_id']).id)
                user_book.pages = book_dict['pages']
                user_book.pages_read = book_dict['pages_read']
                user_book.rate = book_dict['rate']
                user_book.loved = book_dict['loved']
                user_book.snippet = book_dict['snippet']
                user_book.cover_url = book_dict['cover_url']
            except Exception as e:
                user_book = UserBooks(user, book,  book_dict['pages_read'],  book_dict['pages'], book_dict['rate'], book_dict["snippet"])
                user_book.cover_url = book_dict['cover_url']
                db.session.add(user_book)
            db.session.commit()
            books.append(user_book)
        return Response(True, "Books Appended", UserBookSchema(many=True).dumps(books).data).output()
    except Exception as e:
        return Response(False, str(e), None).output()


def delete_book():
    """
    Removes an book from the user. Deletes
    info like pages, paged_read, snippet, and rate.

    @return JSON with success and message

    @see User, UserBooks, Book

    """
    parser = reqparse.RequestParser()
    parser.add_argument("user_id", type=str)
    parser.add_argument("book_name", type=unicode)
    args = parser.parse_args()
    return delete_book_impl(args)

def delete_book_impl(args):
    try:
        book = user_book_from_book_name(args['book_name'], user_by_user_id(args['user_id']).id)
        db.session.delete(book)
        db.session.commit()
        return Response(True, "Book Deleted", None).output()
    except Exception as e:
        return Response(False, str(e), None).output()


def update_book():
    """

    Update an instance of UserBook from the info
    of an user and a book id. It can only update pages,
    pages_read, snippet (that may not change) and rate.

    @see UserBooks

    """
    parser = reqparse.RequestParser()
    parser.add_argument("book_id", type=int, required=False)
    parser.add_argument("user_id", type=str, required=False)
    parser.add_argument("pages", type=int, required=False)
    parser.add_argument("pages_read", type=int, required=False)
    parser.add_argument("snippet", type=unicode, required=False)
    parser.add_argument("cover_url", type=unicode, required=False)
    parser.add_argument("rate", type=float, required=False)
    parser.add_argument("loved", type=bool, required=False)
    parser.add_argument("notes", type=dict, action='append', required=False)
    args = parser.parse_args()
    return update_book_impl(args)


def update_book_impl(args):
    try:
        book = user_book_from_book_id(args['book_id'], user_by_user_id(args['user_id']).id)

        if args.has_key("pages") and args['pages'] is not None:
            book.pages = int(args['pages'])

        if args.has_key("cover_url") and args['cover_url'] is not None:
            book.cover_url = args['cover_url']

        if args.has_key("loved") and args['loved'] is not None:
            book.loved = args['loved']

        if args.has_key("pages_read") and args['pages_read'] is not None:
            book.pages_read = args['pages_read']

        if args.has_key("snippet") and args['snippet'] is not None:
            book.snippet = args['snippet']

        if args.has_key("rate") and args['rate'] is not None:
            book.rate = args['rate']

        if args.has_key("loved") and args['loved'] is not None:
            book.loved = args['loved']

        db.session.commit()
        return Response(True, "Book Updated", UserBookSchema().dumps(book).data).output()
    except Exception as e:
        return Response(False, str(e), None).output()


def list_books():
    """

    Fetch the user entire user book list.

    @see Book

    """
    parser = reqparse.RequestParser()
    parser.add_argument("user_id", type=str, required=True)
    args = parser.parse_args()
    return list_books_impl(args)


def list_books_impl(args):
    try:
        user_books = list_user_books(args['user_id'])
        for user_book in user_books:
            if len(user_book.notes) > 0:
                print(user_book.notes)
        return Response(True, "Book Listed", UserBookSchema(many=True).dumps(user_books).data).output()
    except Exception as e:
        return Response(False, str(e), None).output()


class TopRatedBooksRequest(Resource):
    """

    Fetch top rated books from the anonymous rating given by users
    (Using the red_rating table)

    @see Rating

    """
    def get(self):
        return top_rated_books()


def top_rated_books():
    parser = reqparse.RequestParser()
    args = parser.parse_args()
    return top_rated_books_impl(args)


def top_rated_books_impl(args):
    try:
        books = dao.top_rated_books()
        return json.loads(BookSchema(many=True).dumps(books).data)
    except Exception as e:
        return json.dumps({"error": str(e)})