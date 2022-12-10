"""
Define routes for ambulance APIs
"""
from flask import Blueprint, request, abort
from flask_expects_json import expects_json

from ambulance.schema.ambulance_schema import ambulance_schema
from ambulance.schema.position_schema import position_schema
from ambulance.service.ambulance_service import add_ambulance, list_ambulances, get_near_ambulances


ambulance = Blueprint('ambulance', __name__, url_prefix='/ambulance')

@ambulance.route('/create', methods=['POST'])
@expects_json(ambulance_schema)
def create_ambulance():
    return add_ambulance(request), 201

@ambulance.route('/get', methods=['GET'])
def get_ambulances():
    return list_ambulances()

@ambulance.route('/near', methods=['GET'])
@expects_json(position_schema)
def get_nearby_ambulances():
    return get_near_ambulances(request.json)
