"""
Security entity
"""
secutiry_schema = {
    "type": "object",
    "properties":{
        "user" :{
            "type":"string",
            "minLength": 1,
            "maxLength": 25
        },
        "password" :{
            "type":"string",
            "minLength": 1,
            "maxLength": 25
        }
    },
    "required":[
        "user",
        "password"
    ]
}
