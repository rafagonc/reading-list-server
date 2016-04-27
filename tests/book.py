import unittest
from endpoints.book import append_book_impl
from endpoints.book import top_rated_books_impl
import json


class TestBook(unittest.TestCase):
    args = {}

    def setUp(self):
        pass

    def test_top_rated_books(self):
        books = top_rated_books_impl(self.args)
        assert len(books) > 0



class TestUserBooks(unittest.TestCase):
    args = {}

    def setUp(self):
        self.args = {"books" : [{"name" : "Book", "pages" : 432, "paged_read" : 234, "user_id" : 1, "snippet" : "daosdaopskdaopsdksaopsk", "rate" : 3.2 },
                                {"name" : "Book", "pages" : 432, "paged_read" : 234, "user_id" : 1, "snippet" : "daosdaopskdaopsdksaopsk", "rate" : 3.2 }
                                ]}

    def test_create_books(self):
        response = json.loads(append_book_impl(self.args))
        assert response['success'] is True