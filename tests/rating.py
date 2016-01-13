import unittest
import json
from db import db
from models.book import Book
from endpoints.rating import rating_book_request_impl

class TestRating(unittest.TestCase):
    args = {}

    def setUp(self):
        self.args['book_name'] = "Romeo and Juliet"
        self.args['author_name'] = "William Shakespeare"
        self.args['category_name'] = "Romance"
        self.args['rating'] = 5.0

    def tearDown(self):
        pass

    def test(self):
        json_result = rating_book_request_impl(self.args)
        assert "error" not in json_result
