from flask_restful import Resource, reqparse
from db import  db
from dao.user import user_by_user_id
from models.user import User
from validator.user import validate
from general.response import simple_response
from schemas.user import UserSchema
import json

parser = reqparse.RequestParser()

class UserEndpoint(Resource):
    def post(self):
        return create_new_user()
    def get(self):
        return get_user()
    


def create_new_user():
    parser.add_argument("name", required=True)
    parser.add_argument("user_id", required=True)
    parser.add_argument("auth_token", required=True)
    parser.add_argument("auth_token_secret", required=True)
    args = parser.parse_args()
    return create_new_user_impl(args)


def create_new_user_impl(args):
    try:
        validate(args)

        user = None
        try:
            user = user_by_user_id(args['user_id'])
        except Exception as e:
            user = User()
            user.user_id = args['user_id']
            user.auth_token = args['auth_token']
            user.auth_token_secret = args['auth_token_secret']
            user.name = args['name']
            db.session.add(user)
            db.session.commit()
        return json.loads(UserSchema().dumps(user).data)
    except Exception as e:
        return json.dumps(simple_response(False, str(e)))


def get_user():
    parser.add_argument("user_id", required=True)
    get_user_impl(parser.parse_args())


def get_user_impl(args):
    try:
        return json.loads(UserSchema().dumps(user_by_user_id(args['user_id'])).data)
    except Exception as e:
        return json.dumps(simple_response(False, str(e)))


