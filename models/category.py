

from db import db
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Category(db.Model):
    __tablename__ = 'red_category'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship("Book", backref='category', lazy='dynamic')


    def __init__(self, category_name=None):
        self.name = category_name

    def __repr__(self):
        return self.name

