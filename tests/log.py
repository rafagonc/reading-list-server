

import unittest
from endpoints.log import append_log_impl
from endpoints.log import list_logs_impl
from endpoints.log import update_log_impl
from endpoints.log import delete_log_impl
from .helper import create_log, create_book, create_user
import json


class TestAppendLog(unittest.TestCase):
    args = {}
    user = None


    def setUp(self):
        self.user = create_user("123")
        create_book("Clean Code", "Robert", "Computer")
        self.args = {"user_id" : "123", "logs" : [{"uuid" : "12390-1293", "book_name" : "Clean Code" , "pages" : 20, "date" : "2016-05-03 19:34"}]}


    def testAppend(self):
        response = append_log_impl(self.args)
        assert response['success'] is True


class TestListLog(unittest.TestCase):
    args = {}
    log = None

    def setUp(self):
        user = create_user("121324")
        book = create_book("Clean Code", "Robert", "Computer")
        log = create_log("Clean Code", "121324")

        self.args = {"user_id" : "121324"}

    def test(self):
        response = list_logs_impl(self.args)
        assert response['success'] is True
        assert response['data'][0] is not None


class TestRemoveLog(unittest.TestCase):
    args = {}
    log = None

    def setUp(self):
        user = create_user("65748")
        book = create_book("CleanCode123", "Robert", "Computer")
        self.log = create_log(book.name, user.user_id)
        self.args = {'user_id' : "65748",'log_id' : self.log.id}

    def test(self):
        response = delete_log_impl(self.args)
        assert response['success'] is True


class TestUpdateLog(unittest.TestCase):
    args = {}
    log = None

    def setUp(self):
        user = create_user("657412318")
        book = create_book("CleanCode123", "Robert", "Computer")
        self.log = create_log(book.name, user.user_id)
        self.args = {'user_id': "657412318", 'log_id': self.log.id, "pages" : 123, "date" : "2014/12/4"}

    def test(self):
        response = update_log_impl(self.args)
        assert response['success'] is True
