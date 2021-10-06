import datetime

from app import app
import jwt
from werkzeug.security import check_password_hash
from flask import request, jsonify
from .users import user_by_email
from functools import wraps


def auth():
    email = request.json['email']
    password = request.json['password']
    if not email or not password:
        return jsonify({"message": "Email e Senha são obrigatórios."}), 401

    user = user_by_email(email)
    if not user:
        return jsonify({"message": "user not found", "data": {}}), 401

    if user and check_password_hash(user.password, password):
        token = jwt.encode({"email": user.email, "exp": datetime.datetime.now() + datetime.timedelta(hours=12),
                            "user_type": user.user_type},
                           app.config["SECRET_KEY"], algorithm="HS256")
        return jsonify({"message": "Login   ", "token": token,
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
            current_user = user_by_email(email=data['email'])
            print(current_user)
        except Exception as e:
            print(e)
            print("CAI NA EXCEPTION")
            return jsonify({'message': 'token is invalid or expired', 'data': []}), 401
        return f(current_user, *args, **kwargs)
    return decorated

