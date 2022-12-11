"""
Module for error handling
"""
from jsonschema.exceptions import ValidationError
from werkzeug.exceptions import HTTPException
from flask import jsonify


def handle_exceptions(exception: Exception):
    """
    Handle the exceptions
    """
    result_message = None
    code = None
    name = None
    if isinstance(exception, HTTPException):
        if isinstance(exception.description, ValidationError):
            result_message = exception.description.message
        else:
            result_message = exception.description
        code = exception.code
        name = exception.name
    else:
        result_message = f'internal server error: { str(exception) }'
        code = 500
    response_data = {
        "message": result_message,
        "code": code,
        "name": name
    }
    result = jsonify(response_data)
    result.status = code
    return result
