from db import db
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from dao.author import find_author_with_name
from dao.category import find_category_with_name
from sqlalchemy.sql import func
from sqlalchemy import desc


class Note(db.Model):
    __tablename__ = "red_note"
    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    user_book_id = Column(Integer, ForeignKey('red_user_books.id'))

    def __init__(self, user_book, text):
        self.user_book_id = user_book.id
        self.text = text

    def __str__(self):
        return "Text: " + self.text
