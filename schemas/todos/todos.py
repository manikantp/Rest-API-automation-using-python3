
todo_definition = {
    "type": "object",
    "properties": {
        "userId": { "type": [ "number", "null", "string" ] }, # for some reason the endpoint is sending back string instead of number. Needs testing with a real API
        "id": { "type": [ "number", "null" ] },
        "title": { "type": "string" },
        "completed": { "type": [ "boolean", "string" ] } # for some reason the endpoint is sending back string instead of boolean. Needs testing with a real API
    },
    "required": ["title", "completed"]
}

schema_todo = todo_definition

schema_todos = {
    "type": "array",
    "items": todo_definition
}