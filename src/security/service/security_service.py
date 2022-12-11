"""
Service module for security
"""
from werkzeug.exceptions import Unauthorized, BadRequest
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

def validate_user(user):
    """
    Validate token user
    """
    return user == registered_user["user"]

def validate_token(token):
    """
    Validates de given token
    """
    try:
        encoded = str(token).split('Bearer ')[1]
        decoded_information = jwt.decode(encoded, key=getenv("SECRET_KEY"),
                                        algorithms=["HS256"])
    except DecodeError:
        raise Unauthorized("Invalid token")
    except ExpiredSignatureError:
        raise Unauthorized("Token expired!")
    except Exception:
        raise BadRequest("Validate the token")
    valid_user = validate_user(decoded_information["user"])
    if not valid_user: raise Unauthorized("Permission denied")

def generate_token(user):
    """
    Creates a token
    """
    payload = {
        "user": user,
        "exp": datetime.utcnow() +
            timedelta(seconds=120)
    }
    token = jwt.encode(payload=payload, key=getenv("SECRET_KEY"))
    return jsonify({"token": token})