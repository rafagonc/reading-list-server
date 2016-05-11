import unittest
import json
from helper import create_user
from endpoints.user import create_new_user_impl, get_user_impl

class TestUser(unittest.TestCase):
    args = {}

    def setUp(self):
        self.args = {"name" : "Rafael" , "auth_token" : "123", "auth_token_secret" : "1234567890", "user_id" : "1234567890"}

    def tearDown(self):
        pass

    def test_create_user(self):
        response = create_new_user_impl(self.args)
        assert json.loads(response)['success'] is True


class TestUser(unittest.TestCase):
    args = {}

    def setUp(self):
        create_user("12324576918")
        self.args = {"user_id" : "12324576918"}

    def test(self):
        response = get_user_impl(self.args)

        assert not response.has_key('error')
