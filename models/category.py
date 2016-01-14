from db import db
from sqlalchemy import Column, String, Integer, ForeignKey


class Category(db.Model):
    __tablename__ = 'red_category'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    book_id = Column(Integer, ForeignKey('red_book.id', ondelete='SET NULL'))

    def __init__(self, category_name=None):
        self.name = category_name

    def __repr__(self):
        return self.name

