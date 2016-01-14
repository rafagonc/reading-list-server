

class InvalidBookNameException(Exception):
    def __str__(self):
        return "Invalid Book Name"


class InvalidRatingException(Exception):
    def __str__(self):
        return "Invalid Rating"