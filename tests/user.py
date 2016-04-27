import unittest
import json
from endpoints.user import create_new_user_impl

class TestUser(unittest.TestCase):
    args = {}

    def setUp(self):
        self.args = {"name" : "Rafael" , "auth_token" : "1234567890", "auth_token_secret" : "1234567890", "user_id" : "1234567890"}

    def tearDown(self):
        pass

    def test_create_user(self):
        response = create_new_user_impl(self.args)
        assert json.loads(response)['success'] is True