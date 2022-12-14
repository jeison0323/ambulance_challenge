"""
Security module routes
"""
from werkzeug.exceptions import BadRequest, Unauthorized
from flask import Blueprint, request
from flask_expects_json import expects_json

from security.schema.security_schema import secutiry_schema
from security.service.security_service import generate_token, registered_user
from utils.hash import hash_str

security = Blueprint('token', __name__, url_prefix='/token')

@security.route('/get_token', methods=['POST'])
@expects_json(secutiry_schema)
def get_token():
    user = request.json["user"]
    password = request.json["password"]
    if user is None or user == "":
        raise BadRequest("user is required")
    if password is None or password == "":
        raise BadRequest("password is required")
    if user != registered_user["user"]\
        or hash_str(password) != registered_user["password"]:
        raise Unauthorized("User not allowed")
    return generate_token(user)