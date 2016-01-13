from db import db
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from author import Author
from category import Category


class Book(db.Model):
    __tablename__ = 'red_book'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    authors = relationship("Author", backref='book', lazy='dynamic', cascade='all,delete')
    categories = relationship("Category", backref='book', lazy='dynamic', cascade='all,delete')
    ratings = relationship("Rating", backref='book', lazy='dynamic', cascade='all,delete')

    def __init__(self, name, author_name, category_name):
        self.name = name

        #create relationships
        if author_name is not None:
            self.authors.append(Author(author_name))

        if category_name is not None:
            self.categories.append(Category(category_name))

    def __repr__(self):
        return self.name


