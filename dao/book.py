from db import db
from models.book import Book
from models.rating import Rating
from run import db
from sqlalchemy.sql import func
from sqlalchemy import desc

#queries
def find_book_with_name(book_name):
    return Book.query\
               .filter(Book.name == book_name)\
               .first()

def top_rated_books():
    return db.session.query(Book, func.avg(Rating.rating))\
                     .join(Rating)\
                     .order_by(desc(func.avg(Rating.rating)))\
                     .all()
