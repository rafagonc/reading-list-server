import unittest
from endpoints.book import top_rated_books_impl


class TestBook(unittest.TestCase):
    args = {}

    def setUp(self):
        pass

    def test_top_rated_books(self):
        books = top_rated_books_impl(self.args)
        print books
        assert len(books) > 0