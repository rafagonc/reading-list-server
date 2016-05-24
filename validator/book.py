

from exc.invalid_book import InvalidBookException

def validate(book_dict):
    name = book_dict['name']
    author = book_dict['author']
    category = book_dict['category']
    pages = book_dict['pages']
    pages_read = book_dict['pages_read']
    if len(name) > 0 and len(category) > 0 and pages is not None and pages_read is not None:
        pass
    else:
        raise InvalidBookException()
