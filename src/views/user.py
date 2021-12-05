from flask import Blueprint
from flask import jsonify, make_response, request, abort
from presenter.user import get_users, get_user, add_user

import json


user_views = Blueprint("user", __name__)


@user_views.route('/users', methods=['GET'])
def get_users_view():
    users = map(lambda x: x.serialize(), get_users())
    return make_response(jsonify(list(users)), 200)


@user_views.route('/users/<user_id>')
def get_user_view(user_id):
    user = get_user(user_id)
    if not user:
        return abort(404)

    return make_response(jsonify(user.serialize()), 200)


@user_views.route('/users', methods=['POST'])
def add_user_view():
    data = str(request.get_data(as_text=True))
    data = json.loads(data)

    if "user_name" not in data:
        return abort(400)

    add_user(data["user_name"])
    return make_response("", 201)  # 201 - Created
