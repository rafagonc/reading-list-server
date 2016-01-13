from db import db
from sqlalchemy import Column, String, Integer, ForeignKey


class Author(db.Model):
    __tablename__ = 'red_author'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    book_id = Column(Integer, ForeignKey('red_book.id'))

    def __init__(self, author_name=None):
        self.name = author_name

    def __repr__(self):
        return self.name

