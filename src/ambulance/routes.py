"""
Define routes for ambulance APIs
"""
from werkzeug.exceptions import BadRequest, Unauthorized
from flask import Blueprint, request
from flask_expects_json import expects_json

from security.service.security_service import validate_token
from ambulance.schema.ambulance_schema import ambulance_schema
from ambulance.service.ambulance_service import add_ambulance, list_ambulances, get_near_ambulances


ambulance = Blueprint('ambulance', __name__, url_prefix='/ambulance')

@ambulance.before_request
def verify_token_middleware():
    token = request.headers.get("Authorization")
    if token is None or token == "":
        raise Unauthorized("Missing authorization token")
    validate_token(token)

@ambulance.route('/create', methods=['POST'])
@expects_json(ambulance_schema)
def create_ambulance():
    """
    Create ambulance endpoint
    """
    return add_ambulance(request.json), 201

@ambulance.route('/get', methods=['GET'])
def get_ambulances():
    """
    Endpoint for listing all active ambulances
    """
    return list_ambulances()

@ambulance.route('/near', methods=['GET'])
def get_nearby_ambulances():
    """
    Endpoint for listing all active ambulances
    sorted by proximity
    """
    latitude = request.args.get("latitude", type=float)
    longitude = request.args.get("longitude", type=float)
    if latitude is None:
        raise BadRequest("latitude is required")
    if longitude is None:
        raise BadRequest("longitude is required")
    return get_near_ambulances(latitude, longitude)
