"""
Ambulance entity
"""
position_schema = {
    "type": "object",
    "properties":{
        "latitude": {"type":"number"},
        "longitude": {"type":"number"}
    },
    "required":[
        "latitude",
        "longitude"
    ]
}
