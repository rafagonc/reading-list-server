from db import db
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy import desc


class UserBooks(db.Model):
    __tablename_ = "red_user_books"

    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey("red_user.id"))
    book = Column(Integer, ForeignKey("red_book.id"))
    pages = Column(Integer)
    pages_read = Column(Integer)
    rate = Column(Float)
    snippet = Column(String)
