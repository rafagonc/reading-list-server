

from ma import ma
from marshmallow import fields
from models.book import Book
from schemas.author import AuthorSchema
from schemas.category import CategorySchema

class BookSchema(ma.ModelSchema):
    author = fields.Nested(AuthorSchema)
    category = fields.Nested(CategorySchema)
    rating = fields.Number()

    class Meta:
        fields = ['id','name','author','category','rating']