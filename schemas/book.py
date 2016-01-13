from ma import ma
from models.book import Book

class BookSchema(ma.ModelSchema):
    class Meta:
        model = Book