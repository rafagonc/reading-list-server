from db import db
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy import desc

class User(db.Model):
    __tablename__ = 'red_user'

    id = Column(Integer, primary_key=True)
    user_id = Column(String, unique=True)
    auth_token = Column(String)
    authTokenSecret = Column(String)
    name = Column(String)
    profile_picture = Column(String)