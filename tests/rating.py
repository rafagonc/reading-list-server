

import unittest
import json
from db import db
from models.book import Book
from models.author import Author
from models.category import Category
from endpoints.rating import rating_book_request_impl, multiple_rating_book_request_impl
from dao.author import count_author_with_name
from dao.category import count_category_with_name

class TestRating(unittest.TestCase):
    args = {}
    multiple= {}

    def setUp(self):
        self.args['book_name'] = "Romeo and Juliet"
        self.args['author_name'] = "William Shakespeare"
        self.args['category_name'] = "Romance"
        self.args['rating'] = 5.0

        self.multiple = {"books" : [self.args]}

    def tearDown(self):
        db.session.commit()

    def test_multiple(self):
        json_result = multiple_rating_book_request_impl(self.multiple)

    def test(self):
        json_result = rating_book_request_impl(self.args)
        assert "error" not in json_result

    def test_invalid_book_name(self):
        self.args['book_name'] = None
        json_result = rating_book_request_impl(self.args)
        assert "error" in json_result

    def test_invalid_over_rating(self):
        self.args['rating'] = 6
        json_result = rating_book_request_impl(self.args)
        assert "error" in json_result

    def test_invalid_under_rating(self):
        self.args['rating'] = -1
        json_result = rating_book_request_impl(self.args)
        assert "error" in json_result

    def test_duplicate_author(self):
        author = Author("Rafael")
        db.session.add(author)
        db.session.commit()
        self.args['author_name'] = 'Rafael'
        json_result = rating_book_request_impl(self.args)
        assert "error" not in json_result


    def test_duplicate_category(self):
        category = Category("Sci-fi")
        db.session.add(category)
        db.session.commit()
        self.args['category_name'] = 'Sci-fi'
        json_result = rating_book_request_impl(self.args)
        assert "error" not in json_result

