from ma import ma
from marshmallow import fields
from models.note import Note

class NoteSchema(ma.ModelSchema):
    class Meta:
        fields = ['text', 'id']