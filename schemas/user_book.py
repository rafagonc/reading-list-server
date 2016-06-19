

from ma import ma
from marshmallow import fields
from schemas.book import BookSchema
from schemas.note import NoteSchema

class UserBookSchema(ma.ModelSchema):
    book = fields.Nested(BookSchema)
    notes = fields.Nested(NoteSchema, many=True)

    class Meta:
        fields = ('pages', "pages_read", "snippet", "rate", "book", "id", "loved", "cover_url", 'notes')