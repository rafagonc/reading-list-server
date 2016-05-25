from db import db
from book import Book
from user_books import UserBooks
from sqlalchemy import Column, Integer, ForeignKey, DateTime, String

class ReadingLog(db.Model):
    __tablename__ = 'red_reading_log'

    id = Column(Integer, primary_key=True)
    book = Column(Integer, ForeignKey('red_book.id'))
    user = Column(String, ForeignKey('red_user.user_id'))
    pages = Column(Integer, nullable=False)
    date = Column(DateTime, nullable=False)
    uuid = Column(String, unique=True)

    @property
    def book_ref(self):
        return UserBooks.query.filter(UserBooks.user_id == self.user.id, UserBooks.book_id == self.book).first()

