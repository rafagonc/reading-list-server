from flask_restful import Resource, reqparse
from schemas.log import LogSchema
from db import db
from dao.book import find_book_with_name
from models.log import ReadingLog
from dao.user import user_by_id
from general.response import simple_response
from dateutil.parser import parse
import json

parser = reqparse.RequestParser()
parser.add_argument("logs", type=dict, action='append')
parser.add_argument("user_id", type=int, required=False)

class LogEndpoint(Resource):
    def post(self):
        return append_log()


def append_log():
    args = parser.parse_args()
    return append_log_impl(args)


def append_log_impl(args):
    try:
        user = user_by_id(args['user_id'])
        logs = []
        for log_dict in args['logs']:
            log = ReadingLog()
            log.book = find_book_with_name(log_dict['book_name']).id
            log.date = parse(args['date'])
            log.pages = args['pages']
            db.session.add(log)
        db.session.commit()
        return simple_response(True, "Logs Appended")
    except Exception as e:
        return json.dumps(simple_response(False, str(e)))