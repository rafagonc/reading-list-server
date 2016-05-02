from ma import ma
from models.log import ReadingLog
from marshmallow import fields

class LogSchema(ma.ModelSchema):
    class Meta:
        meta = ReadingLog
