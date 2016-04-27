from flask_restful import Resource, reqparse
from models.user import User
from validator.user import validate
from general.response import simple_response
import json

parser = reqparse.RequestParser()
parser.add_argument("name", required=True)
parser.add_argument("user_id", required=True)
parser.add_argument("auth_token", required=True)
parser.add_argument("auth_token_secret", required=True)

class UserEndpoint(Resource):
    def post(self):
        return create_new_user()

def create_new_user():
    args = parser.parse_args()
    return create_new_user_impl(args)

def create_new_user_impl(args):
    try:
        validate(args)

        user = User()
        user.user_id = args['user_id']
        user.authToken = args['auth_token']
        user.authTokenSecret = args['auth_token_secret']
        user.name = args['name']

        return json.dumps(simple_response(True, "User Created"))
    except Exception as e:
        return json.dumps(simple_response(False, str(e)))
