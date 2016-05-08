from models.user_books import UserBooks
from dao.book import find_book_with_name
from exc.invalid_user_book import UserBookNotFoundException

def user_book_from_book_name(book_name, user_id):
    user_book = UserBooks.query.filter(UserBooks.book_id == find_book_with_name(book_name).id, UserBooks.user_id == user_id).first()
    if user_book is None:
        raise UserBookNotFoundException()
    return user_book


def user_book_from_book_id(book_id, user_id):
    user_book = UserBooks.query.filter(UserBooks.book_id == book_id, UserBooks.user_id == user_id).first()
    if user_book is None:
        raise UserBookNotFoundException()
    return user_book


def list_user_books(user_id):
    list = UserBooks.query.filter(UserBooks.user_id == user_id).all()
    return list