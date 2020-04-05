from app import app
from app.models.user import User
from flask import request, jsonify


@app.route("/test")
def hello_world():

    return "Service 1 API routes is working just fine"


@app.route("/user", methods=["POST"])
def save_user():
    data = request.json 
    name = data["name"]
    surname = data["surname"]
    email = data["email"]

    user = User(name, surname, email)

    user.save()

    saved_user = User.get_user_by_email(email)

    return jsonify(saved_user), 200


@app.route("/users", methods=["GET"])
def get_users():
    users = User.get_all_users()
    return jsonify(users), 200


@app.route("/user/<userid>", methods=["GET"])
def get_user(userid):
    print(userid)

    user = User.get_user(userid)
    return jsonify(user), 200
