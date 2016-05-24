

from db import db
from models.log import ReadingLog


def list_user_logs(user_id):
    return ReadingLog.query.filter(ReadingLog.user.like(user_id)).all()


def log_by_id(log_id):
    return ReadingLog.query.filter(ReadingLog.id == log_id).first()