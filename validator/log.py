

from dao.book import find_book_with_name
from exc.book_not_found import BookNotFoundException
from exc.invalid_log import InvalidLogException

def validate(log_dict):
    pages = log_dict['pages']
    date = log_dict['date']
    book_name = log_dict['book_name']
    if find_book_with_name(book_name) is None:
        raise BookNotFoundException()
    if pages == 0 or len(date) == 0:
        raise InvalidLogException()


