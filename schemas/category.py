

from ma import ma
from marshmallow import fields
from models.category import Category

class CategorySchema(ma.ModelSchema):
    class Meta:
        fields = ['name']