from models.author import Author
from models.category import Category
from db import db


def create_category(name):
    category = Category(name)
    db.session.add(category)
    db.session.commit()


def create_author(name):
    author = Author(name)
    db.session.add(author)
    db.session.commit()