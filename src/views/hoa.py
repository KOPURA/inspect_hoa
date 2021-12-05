from flask import Blueprint
from flask import jsonify, make_response, request, abort
from presenter.hoa import get_hoas, add_hoa

import json


hoa_view = Blueprint("hoa", __name__)


@hoa_view.route('/hoas', methods=['GET'])
def get_hoas_view():
    hoas = map(lambda x: x.serialize(), get_hoas())
    return make_response(jsonify(list(hoas)), 200)


@hoa_view.route('/hoas', methods=['POST'])
def add_hoa_view():
    data = str(request.get_data(as_text=True))
    data = json.loads(data)

    if not all(key in data for key in ("name", "address")):
        return abort(400)  # Wrong data provided

    add_hoa(data["name"], data["address"])
    return make_response("", 201)  # 201 - Created
