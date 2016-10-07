from models.user_books import UserBooks
from dao.book import find_book_with_name
from dao.user import user_by_user_id
from db import db
from models.book import Book
from exc.invalid_user_book import UserBookNotFoundException
from sqlalchemy.sql import func
from .category import find_category_with_name


def user_book_from_book_name(book_name, user_id):
    user_book = UserBooks.query.filter(UserBooks.book_id == find_book_with_name(book_name).id, UserBooks.user_id == user_id).first()
    if user_book is None:
        raise UserBookNotFoundException()
    return user_book


def user_book_from_book_id(book_id, user_id):
    user_book = UserBooks.query.filter(UserBooks.id == book_id, UserBooks.user_id == user_id).first()
    if user_book is None:
        raise UserBookNotFoundException()
    return user_book


def list_user_books(user_id):
    list = UserBooks.query.filter(UserBooks.user_id == user_by_user_id(user_id).id).all()
    return list


def number_of_pages_read_by_user(user_id):
    return db.session.query(func.sum(UserBooks.pages_read)).filter(UserBooks.user_id == user_id).group_by(UserBooks.user_id).scalar()


def number_of_books_completed_by_user(user_id):
    return db.session.query(func.count(UserBooks.user_id)).filter(UserBooks.pages_read == UserBooks.pages_read).group_by(UserBooks.user_id).scalar()


def number_of_books_comleted_by_user_in_category(user_id, category):
    completed_books = db.session.query(func.count(UserBooks.user_id)).join(UserBooks.book_id == Book.id).filter(UserBooks.pages_read == UserBooks.pages_read, Book.category_id == find_category_with_name(category)).group_by(UserBooks.user_id).scalar()
