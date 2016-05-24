from flask_restful import Resource, reqparse
from schemas.log import LogSchema
from db import db
from dao.book import find_book_with_name
from models.log import ReadingLog
from dao.user import user_by_user_id
from general.response import simple_response
from dateutil.parser import parse
from validator.log import validate
from dao.log import list_user_logs
from dao.log import log_by_id
from response import Response
import json

class LogEndpoint(Resource):

    def post(self):
        return append_log()

    def get(self):
        return list_logs()

    def put(self):
        return update_log()

    def delete(self):
        return delete_log()


def append_log():
    """

    Append log to user attached to an book.

    @see ReadingLog

    @return Success and Message

    """
    parser = reqparse.RequestParser()
    parser.add_argument("logs", type=dict, action='append')
    parser.add_argument("user_id", type=str, required=False)
    args = parser.parse_args()
    return append_log_impl(args)


def append_log_impl(args):
    try:
        user = user_by_user_id(args['user_id'])
        logs = []
        if args['logs'] is None:
            return Response(True, "Logs Appended", LogSchema(many=True).dumps(logs).data).output()
        for log_dict in args['logs']:
            validate(log_dict)
            log = None
            if log_dict.has_key('id') and log_dict['id'] is not None:
                log = log_by_id(log_dict['id'])
                if log is None:
                    log = ReadingLog()
            else:
                log = ReadingLog()
            log.book = find_book_with_name(log_dict['book_name']).id
            log.date = parse(log_dict['date'])
            log.pages = log_dict['pages']
            log.user = user.user_id
            db.session.add(log)
            logs.append(log)
        db.session.commit()
        return Response(True, "Logs Appended", LogSchema(many=True).dumps(logs).data).output()
    except Exception as e:
        return Response(False, str(e), None).output()


def list_logs():
    """

    Fetch the list of reading logs from an user

    @return List of logs

    """
    parser = reqparse.RequestParser()
    parser.add_argument("user_id", type=str, required=False)
    args = parser.parse_args()
    return list_logs_impl(args)


def list_logs_impl(args):
    try:
        logs = list_user_logs(args['user_id'])
        return Response(True, "Logs Listed", LogSchema(many=True).dumps(logs).data).output()
    except Exception as e:
        return Response(False, str(e), None).output()


def update_log():
    """

    Update the given log values such as pages or date

    @see ReadingLog

    @:return success dict
    """
    parser = reqparse.RequestParser()
    parser.add_argument("log_id", type=int)
    parser.add_argument("user_id", type=str)
    parser.add_argument("pages", type=int)
    parser.add_argument("date", type=str)
    return update_log_impl(parser.parse_args())


def update_log_impl(args):
    try:
        user = user_by_user_id(args['user_id'])
        log = log_by_id(args['log_id'])
        log.pages = args['pages'] if args['pages'] is not None else log.pages
        log.date = parse(args['date']) if args['date'] is not None else log.date
        db.session.commit()
        return Response(True, "Log Updated", LogSchema().dumps(log).data).output()
    except Exception as e:
        return Response(False, str(e), None).output()


def delete_log():
    """

    Delete a given log by id

    @see Reading Log

    @return success dict

    """
    parser = reqparse.RequestParser()
    parser.add_argument("log_id", type=int)
    parser.add_argument("user_id", type=str)
    return delete_log_impl(parser.parse_args())


def delete_log_impl(args):
    try:
        user = user_by_user_id(args['user_id'])
        log = log_by_id(args['log_id'])
        db.session.delete(log)
        db.session.commit()
        return simple_response(True, "Log Deleted")
    except Exception as e:
        return Response(False, str(e), None).output()
