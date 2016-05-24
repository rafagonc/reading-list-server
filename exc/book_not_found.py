

class BookNotFoundException(Exception):

    def __str__(self):
        return "Book was not found"
