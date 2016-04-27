from db import db
from sqlalchemy import Column, Integer, ForeignKey, DateTime

class ReadingLog(db.Model):
    __tablename__ = 'red_reading_log'

    id = Column(Integer, primary_key=True)
    book = Column(Integer, ForeignKey('red_book.id'))
    pages = Column(Integer, nullable=False)
    date = Column(DateTime, nullable=False)

