from app import app
from app.models.address import Address
from flask import request, make_response, jsonify


@app.route("/test")
def hello():
    return "Service 2 is working just fine"


@app.route("/address", methods=["POST"])
def save_address():
    data = request.json
    street = data["street"]
    city = data["city"]
    province = data["province"]
    user_id = data["user_id"]

    address = Address(street, city, province, user_id)

    address.save_address_to_db()

    return make_response(address.serialize(), 200)


@app.route("/addresses", methods=["GET"])
def get_addresses():
    addresses = Address.get_all_address()

    resp = []

    for address in addresses:
        resp.append(address.serialize())

    return jsonify(resp), 200
