geo_definition = {
        "lat": {"type": "number"},
        "lng": {"type": "number"}
}

address_definition = {
        "street": {"type": "string"},
        "suite": {"type": "string"},
        "city": {"type": "string"},
        "zipcode": {"type": "string"},
        "geo": geo_definition
}

company_definition = {
        "name": {"type": "string"},
        "catchPhrase": {"type": "string"},
        "bs": {"type": "string"}
}

user_definition = {
    "type": "object",
    "properties": {
        "id": {"type": ["number", "null"]},
        "name": {"type": "string"},
        "username": {"type": "string"},
        "email": {"type": "string"},
        "address": address_definition,
        "phone": {"type": "string"},
        "website": {"type": "string"},
        "company": company_definition
    },
    "required": []
}

schema_user = user_definition

schema_users = {
    "type": "array",
    "items": user_definition
}