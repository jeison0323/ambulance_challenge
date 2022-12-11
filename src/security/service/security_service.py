"""
Service module for security
"""
from os import getenv
from datetime import timedelta, datetime
from flask import jsonify
import jwt
from jwt.exceptions import DecodeError, ExpiredSignatureError

from utils.hash import hash_str

registered_user = {
    "user": "test",
    "password": f"{hash_str('test')}"
}

def validate_token(token):
    """
    Validates de given token
    """
    try:
        jwt.decode(token, key=getenv("SECRET_KEY"))
    except DecodeError:
        response = jsonify({"message": "Invalid token!"})
        response.status_code = 401
        return response
    except ExpiredSignatureError:
        response = jsonify({"message": "Token expired!"})
        response.status_code = 401
        return response

def generate_token(user):
    """
    Creates a token
    """
    payload = {
        "user": user,
        "expiration": str(datetime.utcnow() +
            timedelta(seconds=240))
    }
    token = jwt.encode(payload=payload, key=getenv("SECRET_KEY"))
    return jsonify({"token": token})