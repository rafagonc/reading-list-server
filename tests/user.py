import unittest
import json
from helper import create_user
from endpoints.user import create_new_user_impl, get_user_impl, update_user_impl

class TestCreateUser(unittest.TestCase):
    args = {}

    def setUp(self):
        self.args = {"name" : "Rafael" , "auth_token" : "123", "auth_token_secret" : "1234567890", "user_id" : "1234567890"}

    def test_create_user(self):
        response = create_new_user_impl(self.args)
        assert response['success'] is True


class TesGetUser(unittest.TestCase):
    args = {}

    def setUp(self):
        create_user("12324576918")
        self.args = {"user_id" : "12324576918"}

    def test(self):
        response = get_user_impl(self.args)
        assert response['success'] is True


class TestUpdateUser(unittest.TestCase):
    args = {}
    user = None

    def setUp(self):
        self.user = create_user("87656")
        self.args = {"name" : "Rafael2" , "auth_token" : "123", "auth_token_secret" : "1234567890", "user_id" : "87656"}

    def test_create_user(self):
        response = update_user_impl(self.args)
        assert response['success'] is True
        assert self.user.name == "Rafael2"
