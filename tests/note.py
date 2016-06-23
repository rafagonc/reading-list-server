import unittest
from db import db
from endpoints.note import create_note_impl, update_note_impl, remove_note_impl
from helper import create_user, create_book, create_user_book, create_note
from models.note import Note


class TestCreateNote(unittest.TestCase):
    args = {}
    user_book = None

    def setUp(self):
        book = create_book("Clean Code1", "Roberto", "Computer")
        user = create_user("123121")
        self.user_book = create_user_book(user, book)
        self.args['book_id'] = book.id
        self.args['user_id'] = user.id
        self.args['text'] = "Teste"

    def tearDown(self):
        pass

    def test(self):
        response = create_note_impl(self.args)
        assert response['success'] is True


class TestUpdateNote(unittest.TestCase):
    args = {}
    user_book = None

    def setUp(self):
        book = create_book("Clean Code1", "Roberto", "Computer")
        user = create_user("kdpao-")
        self.user_book = create_user_book(user, book)
        note = create_note(self.user_book)
        self.args = {"note_id" : note.id, "text" : "daskdopaskdpoaskdpoaks"};

    def tearDown(self):
        pass

    def test(self):
        resposne = update_note_impl(self.args)
        assert resposne['data']['text'] == self.args['text']
        assert resposne['success'] is True


class TestDeleteNote(unittest.TestCase):
    args = {}
    user_book = None
    note = None

    def setUp(self):
        book = create_book("Clean Code1", "Roberto", "Computer")
        user = create_user("312-0asd")
        self.user_book = create_user_book(user, book)
        self.note = create_note(self.user_book)
        self.args = {"note_id" : self.note.id}

    def tearDown(self):
        pass

    def test(self):
        resposne = remove_note_impl(self.args)
        assert self.note not in self.user_book.notes
        assert resposne['success'] is True
