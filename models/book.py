from db import db
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from author import Author
from category import Category
from dao.author import find_author_with_name
from dao.category import find_category_with_name


class Book(db.Model):
    __tablename__ = 'red_book'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    authors = relationship("Author", backref='book', lazy='dynamic', cascade='all,delete')
    categories = relationship("Category", backref='book', lazy='dynamic', cascade='all,delete')
    ratings = relationship("Rating", backref='book', lazy='dynamic', cascade='all,delete')

    def __init__(self, name, author_name, category_name):
        self.name = name

        #author
        if author_name is not None:
            author = find_author_with_name(author_name)
            if author is None:
                author = Author(author_name)
            self.authors.append(author)

        #category
        if category_name is not None:
            category = find_category_with_name(category_name)
            if category is None:
                category =  Category(category_name)
            self.categories.append(category)

    def __repr__(self):
        return self.name


