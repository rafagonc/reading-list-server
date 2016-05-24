

class UserNotFoundException(Exception):

    def __str__(self):
        return "User was not found"
