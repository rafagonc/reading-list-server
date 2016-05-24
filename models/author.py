

from db import db
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Author(db.Model):
    __tablename__ = 'red_author'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship("Book", backref='author', lazy='dynamic')

    def __init__(self, author_name=None):
        self.name = author_name

    def __repr__(self):
        return self.name

