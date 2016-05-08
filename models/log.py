from db import db
from book import Book
from sqlalchemy import Column, Integer, ForeignKey, DateTime, String

class ReadingLog(db.Model):
    __tablename__ = 'red_reading_log'

    id = Column(Integer, primary_key=True)
    book = Column(Integer, ForeignKey('red_book.id'))
    user = Column(String, ForeignKey('red_user.user_id'))
    pages = Column(Integer, nullable=False)
    date = Column(DateTime, nullable=False)

    @property
    def book_ref(self):
        return Book.query.filter(Book.id == self.book).first()
