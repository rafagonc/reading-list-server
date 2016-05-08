from db import db
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from models.book import Book
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy import desc


class UserBooks(db.Model):
    __tablename_ = "red_user_books"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("red_user.id"))
    book_id = Column(Integer, ForeignKey("red_book.id"))
    pages = Column(Integer)
    pages_read = Column(Integer)
    rate = Column(Float)
    snippet = Column(String)

    def __init__(self, user, book, pages_read=0, pages=0, rate=0, snippet=""):
        self.user_id = user.id
        self.book_id = book.id
        self.pages = pages
        self.pages_read = pages_read
        self.rate = rate
        self.snippet = snippet


    @property
    def book(self):
        return Book.query.filter(Book.id == self.book_id).first()
