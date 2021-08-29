import datetime

from app import app
import jwt
from werkzeug.security import check_password_hash
from flask import request, jsonify
from .users import user_by_username
from functools import wraps


def auth():
    user_auth = request.authorization
    if not user_auth or not user_auth.username or not user_auth.password:
        return jsonify({"message": "could not verify", "WWW-Authenticate": "Basic auth='Login required'"}), 401

    user = user_by_username(user_auth.username)
    if not user:
        return jsonify({"message": "user not found", "data": {}}), 401

    if user and check_password_hash(user.password, user_auth.password):
        token = jwt.encode({"username": user.username, "exp": datetime.datetime.now() + datetime.timedelta(hours=12)},
                           app.config["SECRET_KEY"], algorithm="HS256")
        return jsonify({"message": "Validated successfully", "token": token,
                        "exp": datetime.datetime.now() + datetime.timedelta(hours=12)})

    return jsonify({"message": "could not verify", "WWW-Authenticate": 'Basic auth="Login required"'}), 401


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers['Authorization']
        if not token:
            return jsonify({'message': 'token is missing', 'data': []}), 401
        try:
            data = jwt.decode(token[7:], app.config['SECRET_KEY'], algorithms="HS256")
            current_user = user_by_username(username=data['username'])
            print(current_user)
        except Exception as e:
            print(e)
            print("CAI NA EXCEPTION")
            return jsonify({'message': 'token is invalid or expired', 'data': []}), 401
        return f(current_user, *args, **kwargs)
    return decorated

