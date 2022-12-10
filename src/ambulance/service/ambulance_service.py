from uuid import uuid4
from flask import jsonify

ambulances = []

def add_ambulance(request):
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
    active_ambulances = filter(lambda ambulance: ambulance["status"] == "ACTIVA", ambulances)
    return list(active_ambulances)
