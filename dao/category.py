from db import db
from models.category import Category

#queries
def find_category_with_name(category_name):
    return Category.query\
               .filter(Category.name == category_name)\
               .first()


def count_category_with_name(category_name):
    return Category.query\
            .filter(Category.name == category_name)\
            .count()
