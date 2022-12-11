"""
Module for error handling
"""
from flask import Blueprint, json

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(400)
def bad_request_handler(error):
    """
    Error handling for 400 http exceptions
    """
    response = error.get_response()
    response.data = json.dumps({
        "code": str(error.code),
        "name": str(error.name),
        "description": str(error.description),
    })
    response.content_type = "application/json"
    return response

@errors.app_errorhandler(404)
def not_found_handler(error):
    """
    Error handling for 404 http exceptions
    """
    response = error.get_response()
    response.data = json.dumps({
        "code": str(error.code),
        "name": str(error.name),
        "description": str(error.description),
    })
    response.content_type = "application/json"
    return response
