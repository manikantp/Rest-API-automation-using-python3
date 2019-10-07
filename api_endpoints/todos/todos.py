from api_client.api_client import ApiClient
import utilities.custom_logger as cl
from schemas.todos.todos import schema_todo, schema_todos

class Todos(ApiClient):
    log = cl.customLogger()

    def __init__(self):
        super(Todos, self).__init__(self.__class__.__name__)
        self.url = 'https://jsonplaceholder.typicode.com/todos'

    def createTodo(self, new_todo):
        return self.create(new_todo)

    def readTodo(self, _id):
        return self.read(_id)

    def updateTodo(self, _id, updated_todo):
        return self.update(_id, updated_todo)

    def deleteTodo(self, _id):
        return self.remove(_id)

    def validateResponseVsSchema(self, jsonResponce, schema=schema_todo):
         return self.validateJsonResponseVsSchema(jsonResponce, schema)
