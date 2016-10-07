

class AbstractClassException(Exception):

    def __str__(self):
        return "This is an abstract class and cannot have abstract methods called"
