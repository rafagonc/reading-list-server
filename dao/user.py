from db import db
from models.user import User
from exc.user_not_find import UserNotFoundException

def user_by_id(user_id):
    user = User.query.filter(User.id == user_id).first()
    if user is None:
        raise UserNotFoundException()
    return user