import unittest
from db import db
from endpoints.book import delete_book_impl, update_book_impl, top_rated_books_impl, append_book_impl, list_books_impl
from dao.user_book import user_book_from_book_name
from helper import create_user, create_book
from models.user_books import  UserBooks
import json


class TestTopRatedBook(unittest.TestCase):
    args = {}

    def setUp(self):
        pass

    def test_top_rated_books(self):
        books = top_rated_books_impl(self.args)


class TestAppendBook(unittest.TestCase):
    args = {}

    def setUp(self):
        create_user("1")
        self.args = {"user_id" : "1", "books" : [{"name" : "Book", "author" : "Barney", "category" : "Romance","pages" : 432, "pages_read" : 234, "snippet" : "daosdaopskdaopsdksaopsk", "rate" : 3.2 },
                                {"name" : "Book", "pages" : 432, "author" : "Barney", "category" : "Romance", "pages_read" : 234, "snippet" : "daosdaopskdaopsdksaopsk", "rate" : 3.2 }
                                ]}

    def test_create_books(self):
        response = json.loads(append_book_impl(self.args))
        assert response['success'] is True


class TestRemoveBook(unittest.TestCase):
    args = {}
    user = None

    def setUp(self):
        self.user = create_user("312")
        book = create_book("Clean Code123", "Robert", "Computer")
        user_book = UserBooks(self.user, book)
        db.session.add(user_book)
        db.session.commit()
        self.args = {"user_id" : self.user.id, "book_name" : book.name}

    def test(self):
        resposne = json.loads(delete_book_impl(self.args))
        assert resposne['success'] is True


class TestUpdateBook(unittest.TestCase):
    args = {}
    user_book = None

    def setUp(self):
        user = create_user("2131")
        book = create_book("Clean Code123", "Robert", "Computer")
        self.user_book = UserBooks(user, book)
        db.session.add(self.user_book)
        db.session.commit()
        self.args = {"user_id" : user.id, "pages_read" : 123, "pages" : 321, "book_id" : book.id}

    def test(self):
        resposne = json.loads(update_book_impl(self.args))
        assert self.user_book.pages == 321 and self.user_book.pages_read == 123.
        assert resposne['success'] is True


class TestListUserBooks(unittest.TestCase):
    args = {}
    user_book = None

    def setUp(self):
        user = create_user("098")
        book = create_book("Clean Code", "Robert", "Computer")
        self.user_book = UserBooks(user, book)
        db.session.add(self.user_book)
        db.session.commit()
        self.args = {'user_id' : user.id}

    def test(self):
        response = list_books_impl(self.args)
        assert response[0] is not None