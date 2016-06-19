from db import db
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Boolean
from sqlalchemy.orm import relationship
from models.book import Book
from sqlalchemy.ext.hybrid import hybrid_property
from models.note import Note


class UserBooks(db.Model):
    __tablename__ = "red_user_books"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("red_user.id"))
    book_id = Column(Integer, ForeignKey("red_book.id"))
    pages = Column(Integer)
    pages_read = Column(Integer)
    rate = Column(Float)
    loved = Column(Boolean)
    snippet = Column(String)
    cover_url = Column(String)
    notes = relationship("Note", backref='user_book', lazy='dynamic')


    def __init__(self, user, book, pages_read=0, pages=0, rate=0, snippet=""):
        self.user_id = user.id
        self.book_id = book.id
        self.pages = pages
        self.pages_read = pages_read
        self.rate = rate
        self.snippet = snippet

    @hybrid_property
    def book(self):
        return Book.query.filter(Book.id == self.book_id).first()

    def add_notes(self, notes_dicts):
        for note_dict in notes_dicts:
            note = None
            if note_dict.has_key('id'):
                notes = filter(lambda x: x.id == note_dict['id'], self.notes)
                if len(notes) > 0:
                    note = notes[0]
                else:
                    note = Note(self, note_dict['text'])
                    self.notes.append(note)
                    db.session.add(note)
            else:
                note = Note(self, note_dict['text'])
                self.notes.append(note)
                db.session.add(note)
            note.text = note_dict['text']
            db.session.commit()
