from db import db
from models.book import Book

#queries
def find_book_with_name(book_name):
    return Book.query\
               .filter(Book.name == book_name)\
               .first()
