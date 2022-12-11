"""
Ambulance service module
"""
from uuid import uuid4
from flask import jsonify, abort

from utils.position import closest

ambulances = []

def add_ambulance(request):
    """
    Creates an ambulance and
    returns a confirmation message
    """
    ambulance = {
        "license_plate": request.json['license_plate'],
        "zone": request.json['zone'],
        "id": str(uuid4()),
        "status": request.json['status'],
        "latitude": request.json['latitude'],
        "longitude": request.json['longitude']
    }
    ambulances.append(ambulance)
    return jsonify({"message": "Ambulance successfully inserted"})

def list_ambulances():
    """
    Returns a list with all active ambulances
    """
    active_ambulances = filter(lambda ambulance: ambulance["status"] == "ACTIVA", ambulances)
    return list(active_ambulances)

def get_near_ambulances(request):
    """
    Return a list with all active ambulances
    sorted by proximity
    """
    if request['latitude'] is None \
        or request['latitude'] == '':
        abort(400)
    if request['longitude'] is None \
        or request['longitude'] == '':
        abort(400)
    ordered_ambulances = []
    to_order_ambulances = list_ambulances()
    for i in range(len(to_order_ambulances)):
        near = closest(to_order_ambulances, request)
        ordered_ambulances.append(near)
        to_order_ambulances.remove(near)
    return ordered_ambulances
