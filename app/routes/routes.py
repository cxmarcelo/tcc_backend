from app import app
from flask import jsonify
from ..views import users, helper


@app.route("/", methods=['GET'])
def root():
    return jsonify({'message': "API Started"})


@app.route("/users", methods=['POST'])
def post_user():
    return users.post_user()


@app.route("/users/<user_id>", methods=['PUT'])
def update_user(user_id):
    return users.update_user(user_id)


@app.route("/users", methods=['GET'])
def get_users():
    return users.get_users()


@app.route("/users/<user_id>", methods=['GET'])
@helper.token_required
def get_user(current_user, user_id):
    return users.get_user(user_id)


@app.route("/users/<user_id>", methods=['DELETE'])
def delete_user(user_id):
    return users.delete_user(user_id)


@app.route("/auth", methods=['POST'])
def authenticate():
    return helper.auth()
