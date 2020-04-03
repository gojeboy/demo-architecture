from app import app
from app.models.user import User
from flask import request, jsonify


@app.route("/test")
def hello_world():

    return "Service 1 API routes is working just fine"


@app.route("/user", methods=["POST"])
def save_user():
    data = request.json
    print(data)
    name = data["name"]
    surname = data["surname"]

    user = User(name, surname)

    user.save()

    return user.serialize(), 200


@app.route("/users", methods=["GET"])
def get_users():
    users = User.get_all_users()
    response = []

    for user in users:
        response.append(user.serialize())

    return jsonify(response), 200


@app.route("/user/<userid>", methods=["GET"])
def get_user(userid):
    return {"id": 1, "name": "Njabulo", "surname": "Nsibande"}, 200
