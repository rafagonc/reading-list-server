from ma import ma
from marshmallow import fields
from models.author import Author

class AuthorSchema(ma.ModelSchema):
    class Meta:
        fields = ['name']