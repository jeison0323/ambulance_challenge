"""
Ambulance service module
"""
import copy
from uuid import uuid4
from flask import jsonify

from utils.position import distance

ambulances = [
    {
        "id": "b2270243-209f-44d2-a362-0f9a1ec06f4c",
        "latitude": 6.2443382,
        "license_plate": "LNJ456",
        "longitude": -75.573553,
        "is_active": True,
        "zone": "Medellin"
    },
    {
        "id": "cdc7638b-1e3d-4c5c-8940-edac2a28c9a7",
        "latitude": 4.999023676713861,
        "license_plate": "ABC456",
        "longitude": -75.53148317974049,
        "is_active": True,
        "zone": "Manizales"
    },
    {
        "id": "4c3e4f04-0beb-4001-8999-8875c00a8ca1",
        "latitude": 4.3108781369148375,
        "license_plate": "JEI323",
        "longitude": -75.26504098477379,
        "is_active": True,
        "zone": "Ibague"
    },
    {
        "id": "7bf4d859-ea1d-4d71-a38a-1bca67ab4f05",
        "latitude": 4.587221409269631,
        "license_plate": "ARC323",
        "longitude": -73.73650418208022,
        "is_active": False,
        "zone": "Bogota"
    }
]

def add_ambulance(ambulance_data):
    """
    Creates an ambulance and
    returns a confirmation message
    """
    ambulance = {
        "license_plate": ambulance_data['license_plate'],
        "zone": ambulance_data['zone'],
        "id": str(uuid4()),
        "is_active": ambulance_data['is_active'],
        "latitude": ambulance_data['latitude'],
        "longitude": ambulance_data['longitude']
    }
    ambulances.append(ambulance)
    return jsonify({"message": "Ambulance successfully inserted"})

def list_ambulances():
    """
    Returns a list with all active ambulances
    """
    active_ambulances = filter(lambda ambulance: ambulance["is_active"], ambulances)
    return copy.deepcopy(list(active_ambulances))

def get_near_ambulances(latitude, longitude):
    """
    Return a list with all active ambulances
    sorted by proximity
    """
    to_order_ambulances = list_ambulances()
    for ambulance in to_order_ambulances:
        amb_latitude = ambulance["latitude"]
        amb_longitude = ambulance["longitude"]
        ambulance["distance"] = distance(latitude, longitude,
            amb_latitude, amb_longitude)
    return sorted(to_order_ambulances, key=lambda amb: amb["distance"])
