from db import db
from models.author import Author

#queries
def find_author_with_name(book_name):
    return Author.query\
               .filter(Author.name == book_name)\
               .first()


def find_author_or_create_with_name(book_name):
    author = Author.query\
               .filter(Author.name == book_name)\
               .first()
    if author is None:
        author = Author()


def count_author_with_name(author_name):
    return Author.query\
            .filter(Author.name == author_name)\
            .count()
