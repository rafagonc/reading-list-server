

class UserBookNotFoundException(Exception):

    def __str__(self):
        return "User book was not found"
