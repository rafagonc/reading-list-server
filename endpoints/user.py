

from flask_restful import Resource, reqparse
from db import  db
from dao.user import user_by_user_id
from models.user import User
from validator.user import validate
from general.response import simple_response
from schemas.user import UserSchema
from response import Response
import json


class UserEndpoint(Resource):
    """

    Controls the CRUD of the User model

    @see User

    """
    def post(self):
        return create_new_user()

    def get(self):
        return get_user()

    def put(self):
        return update_user()

    def delete(self):
        return delete_user()


def create_new_user():
    """

    Create a new user based on the info
    given by Twitter's Digits Kit.

    @see User

    """
    parser = reqparse.RequestParser()
    parser.add_argument("name")
    parser.add_argument("user_id",required=True)
    parser.add_argument("auth_token")
    parser.add_argument("auth_token_secret")
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
            db.session.add(user)
        user.auth_token = args['auth_token']
        user.auth_token_secret = args['auth_token_secret']
        user.name = args['name']
        db.session.commit()
        return Response(True, "User Created", UserSchema().dumps(user).data).output()
    except Exception as e:
        return Response(False, str(e), None).output()


def get_user():
    """

    Return an given user based on the
    user_id.

    @see User

    """
    parser = reqparse.RequestParser()
    parser.add_argument("user_id", required=True)
    return get_user_impl(parser.parse_args())


def get_user_impl(args):
    try:
        return Response(True, "User Listed", UserSchema().dumps(user_by_user_id(args['user_id'])).data).output()
    except Exception as e:
        return Response(False, str(e), None).output()


def update_user():
    """

    Capture any input came from request and set
    on the user if appliable.

    @see User

    """
    parser = reqparse.RequestParser()
    parser.add_argument("name")
    parser.add_argument("user_id", required=True)
    parser.add_argument("auth_token")
    parser.add_argument("auth_token_secret")
    return update_user_impl(parser.parse_args())


def update_user_impl(args):
    try:
        user = user_by_user_id(args['user_id'])

        if args['auth_token'] is not None:
            user.auth_token = args['auth_token']

        if args['auth_token_secret'] is not None:
            user.auth_token_secret = args['auth_token_secret']

        if args['name'] is not None:
            user.name = args['name']

        db.session.commit()
        return Response(True, "User Updated", UserSchema().dumps(user).data).output()
    except Exception as e:
        return Response(False, str(e), None).output()


def delete_user():
    """

    Delete a given user.

    @see User

    """
    parser = reqparse.RequestParser()
    parser.add_argument("user_id", required=True)
    return delete_user_impl(parser.parse_args())


def delete_user_impl(args):
    try:
        db.session.delete(user_by_user_id(args['user_id']))
        return Response(True, "User Deleted", None).output()
    except Exception as e:
        return Response(False, str(e), None).output()
