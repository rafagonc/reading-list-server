

from ma import ma
from models.log import ReadingLog
from marshmallow import fields
from user_book import UserBookSchema

class LogSchema(ma.ModelSchema):
    book_ref = fields.Nested(UserBookSchema)

    class Meta:
        fields = ['pages', 'date', 'user', 'book_ref', 'id', 'uuid']
