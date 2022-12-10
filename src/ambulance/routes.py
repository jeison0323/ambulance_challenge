"""
Define routes for ambulance APIs
"""
from flask import Blueprint, request
from flask_expects_json import expects_json

from ambulance.schema.ambulance_schema import ambulance_schema
from ambulance.service.ambulance_service import add_ambulance, list_ambulances


ambulance = Blueprint('ambulance', __name__, url_prefix='/ambulance')

@ambulance.route('/create', methods=['POST'])
@expects_json(ambulance_schema)
def create_ambulance():
    return add_ambulance(request), 201

@ambulance.route('/get', methods=['GET'])
def get_ambulances():
    return list_ambulances()
