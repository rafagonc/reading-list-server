

from ma import ma
from models.log import ReadingLog
from marshmallow import fields
from book import BookSchema

class LogSchema(ma.ModelSchema):
    book_ref = fields.Nested(BookSchema)

    class Meta:
        fields = ['pages', 'date', 'user', 'book_ref', 'id', 'uuid']
