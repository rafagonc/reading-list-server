from run import app
import unittest

with app.app_context():
    from tests.rating import *
    from tests.book import *
    from tests.user import *
    unittest.TestProgram()
