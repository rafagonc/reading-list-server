from run import app
import unittest

with app.app_context():
    from tests.rating import *
    unittest.TestProgram()
