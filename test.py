from run import app
from db import db
import unittest

with app.app_context():
    from tests.rating import *
    from tests.book import *
    from tests.user import *
    from tests.log import *
    import models
    db.drop_all()
    db.create_all()
    unittest.TestProgram()
