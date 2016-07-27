from dao.note import note_from_id
from dao.user_book import user_book_from_book_id
from db import db
from flask_restful import Resource, reqparse
from models.note import Note
from response import Response
from schemas.note import NoteSchema
from validator.note import validate
from dao.user_book import user_by_user_id

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
    parser.add_argument("text", type=unicode)
    args = parser.parse_args()
    return create_note_impl(args)


def create_note_impl(args):
    try:
        validate(args)
        note = Note(user_book_from_book_id(args["book_id"], user_by_user_id(args['user_id']).id), args['text'])
        db.session.add(note)
        db.session.commit()
        return Response(True, "", NoteSchema().dumps(note).data).output()
    except Exception, e:
        return Response(False, str(e), None).output()


def update_note():
    parser = reqparse.RequestParser()
    parser.add_argument("note_id", type=int)
    parser.add_argument("text", type=unicode)
    args = parser.parse_args()
    return update_note_impl(args)


def update_note_impl(args):
    try:
        note = note_from_id(args['note_id'])
        print(args)
        print(note)
        note.text = args['text']
        db.session.commit()
        return Response(True, "", NoteSchema().dumps(note).data).output()
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
