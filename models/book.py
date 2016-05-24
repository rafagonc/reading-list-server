

from db import db
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from author import Author
from rating import Rating
from category import Category
from dao.author import find_author_with_name
from dao.category import find_category_with_name
from sqlalchemy.sql import func
from sqlalchemy import desc

class Book(db.Model):
    __tablename__ = 'red_book'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    author_id = Column(Integer, ForeignKey('red_author.id', ondelete='SET NULL'))
    category_id = Column(Integer, ForeignKey("red_category.id", ondelete='SET NULL') )
    ratings = relationship("Rating", backref='book', lazy='dynamic', cascade='all,delete')

    def __init__(self, name, author_name, category_name):
        self.name = name

        #author
        if author_name is not None:
            author = find_author_with_name(author_name)
            if author is None:
                author = Author(author_name)
            author.books.append(self)

        #category
        if category_name is not None:
            category = find_category_with_name(category_name)
            if category is None:
                category =  Category(category_name)
            category.books.append(self)

    def rating(self):
         return db.session.query(func.avg(Rating.rating))\
                    .filter(Rating.book_id == self.id)\
                    .group_by(Rating.book_id)\
                    .scalar()

    def __repr__(self):
        return self.name


