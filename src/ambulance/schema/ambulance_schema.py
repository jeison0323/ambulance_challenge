"""
Ambulance entity
"""
ambulance_schema = {
    "type": "object",
    "properties":{
        "license_plate" :{
            "type":"string",
            "pattern": "[a-z]{3}|[A-Z]{3}[0-9]{3}",
            "minLength": 6,
            "maxLength": 6
        },
        "zone" :{
            "type":"string",
            "minLength": 3
        },
        "status" :{
            "type":"string",
            "pattern":"^(ACTIVA)$|^(INACTIVA)$"
        },
        "latitude": {"type":"number"},
        "longitude": {"type":"number"}
    },
    "required":[
        "license_plate",
        "zone",
        "status",
        "latitude",
        "longitude"
    ]
}
