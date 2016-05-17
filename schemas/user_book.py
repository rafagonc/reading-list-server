from ma import ma
from marshmallow import fields
from schemas.book import BookSchema

class UserBookSchema(ma.ModelSchema):
    book = fields.Nested(BookSchema)

    class Meta:
        fields = ('pages', "pages_read", "snippet", "rate", "book", "id", "loved")