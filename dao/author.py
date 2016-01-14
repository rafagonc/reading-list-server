from db import db
from models.author import Author

#queries
def find_author_with_name(book_name):
    return Author.query\
               .filter(Author.name == book_name)\
               .first()


def count_author_with_name(author_name):
    return Author.query\
            .filter(Author.name == author_name)\
            .count()
