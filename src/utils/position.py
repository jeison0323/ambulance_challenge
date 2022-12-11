"""
Position module
"""
from math import cos, asin, sqrt

def distance(request_lat, request_lon, amb_lat, amb_lon):
    """
    Calculate the distant difference between
    2 given latitudes and longitudes.
    """
    divided_pi = 0.017453292519943295
    hav = 0.5 - cos((amb_lat-request_lat)*divided_pi)/2 + \
        cos(request_lat*divided_pi)*cos(amb_lat*divided_pi) *\
            (1-cos((amb_lon-request_lon)*divided_pi)) / 2
    return 12742 * asin(sqrt(hav))

def closest(ambulances, request):
    """
    Returns the closest element for
    the given latitude and longitude
    """
    return min(ambulances, key=lambda amb: distance(request['latitude'],request['longitude'],
        amb['latitude'],amb['longitude']))
