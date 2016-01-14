from db import db
from sqlalchemy import Column, Float, Integer, ForeignKey


class Rating(db.Model):
    __tablename__ = 'red_rating'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('red_book.id',  ondelete='SET NULL'))
    rating = Column(Float)

    def __init__(self, rating, book):
        self.rating = rating
        self.book_id = book.id

    def __repr__(self):
        return self.name

