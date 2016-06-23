from flask_restful import Resource, reqparse
from schemas.book import BookSchema
from dao.user import user_by_id
from db import db
from models.note import Note
from models.book import Book
from models.user_books import UserBooks
from schemas.note import NoteSchema
from dao import book as dao
from validator.note import validate
from dao.note import note_from_id
from dao.user import user_by_user_id
from dao.user_book import  user_book_from_book_id, user_book_from_book_name, list_user_books
from response import Response
import json

class NoteEndpoint(Resource):

	def post(self):
		return create_note()

	def put(self):
		return update_note()

	def delete(self):
		return remove_note()


def create_note():
	parser = reqparse.RequestParser()
    parser.add_argument("book_id", type=int)
    parser.add_argument("user_id", type=str)
    parser.add_argument("text", type=str)
    args = parser.parse_args()
    return create_note_impl(args)

def create_note_impl(args):
	try:
		validate(note)
		note = Note(user_book_from_book_id(args["book_id"]), args['text'])
		db.session.add(note)
		db.session.commit()
		return Response(True, "", NoteSchema().dumps(note).data).output()
	except Exception, e:
        return Response(False, str(e), None).output()

def update_note():
	parser = reqparse.RequestParser()
    parser.add_argument("note_id", type=int)
    parser.add_argument("text", type=str)
    args = parser.parse_args()
    return update_note_impl(args)

def update_note_impl(args):
	try:
		note = note_from_id(args['note_id'])
		note.text = text
		db.session.commit()
		return Response(True, "", None).output()
	except Exception, e:
        return Response(False, str(e), None).output()

def remove_note():
	parser = reqparse.RequestParser()
    parser.add_argument("note_id", type=int)
    args = parser.parse_args()
    return remove_note_impl(args)

def remove_note_impl(args):
	try:
		note = note_from_id(args['note_id'])
		db.session.delete(note)
		db.session.commit()
		return Response(True, "", None).output()
	except Exception, e:
        return Response(False, str(e), None).output()

		