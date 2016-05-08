from models.author import Author
from models.category import Category
from models.book import Book
from models.log import ReadingLog
from models.user import User
from dao.book import find_book_with_name
from db import db


def create_category(name):
    category = Category(name)
    db.session.add(category)
    db.session.commit()
    return category


def create_author(name):
    author = Author(name)
    db.session.add(author)
    db.session.commit()
    return author


def create_book(name, author, category):
    book = Book(name, author, category)
    db.session.add(book)
    db.session.commit()
    return book


def create_log(book_name, user_id):
    log = ReadingLog()
    log.user = user_id;
    log.book = find_book_with_name(book_name).id
    log.pages = 30;
    log.date = "12/12/2014"
    db.session.add(log)
    db.session.commit()
    return log


def create_user(user_id):
    user = User()
    user.name = "das"
    user.user_id = user_id
    db.session.add(user)
    db.session.commit()
    return user