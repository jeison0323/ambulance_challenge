from math import cos, asin, sqrt

def distance(request_lat, request_lon, amb_lat, amb_lon):
    p = 0.017453292519943295
    hav = 0.5 - cos((amb_lat-request_lat)*p)/2 + \
        cos(request_lat*p)*cos(amb_lat*p) * (1-cos((amb_lon-request_lon)*p)) / 2
    return 12742 * asin(sqrt(hav))

def closest(ambulances, request):
    return min(ambulances, key=lambda amb: distance(request['latitude'],request['longitude'],
        amb['latitude'],amb['longitude']))
