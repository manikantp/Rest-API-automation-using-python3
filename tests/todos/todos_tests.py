import pytest
from api_endpoints.todos.todos import Todos
from utilities.teststatus import TestStatus
import utilities.constants.status_codes as StatusCode

class TestTodos():

    @pytest.fixture(autouse = True)
    def classSetup(self):
        self.api = Todos()
        self.ts = TestStatus()

    @pytest.fixture
    def todo_id(self):
        return 1

    @pytest.fixture
    def new_todo(self):
        return {
            'title': "todo title",
            'completed': False
            }

    @pytest.fixture
    def updated_todo(self):
        return {
            'title': "updated todo title",
            'completed': True
            }

    # CRUD operations
    #  CREATE
    def test_create_todo(self, request, new_todo):
        response = self.api.createTodo(new_todo)
        result1 = self.api.verifyStatusCode(response.status_code, StatusCode.CREATED)
        self.ts.mark(result1, "Status code is correct")

        result2 = self.api.validateResponseVsSchema(response.json())
        self.ts.markFinal(request.node.name, result2, "Schema is valid")

    #  READ
    def test_read_one_todo(self, request, todo_id):
        response = self.api.readTodo(todo_id)

        result1 = self.api.verifyStatusCode(response.status_code, StatusCode.OK)
        self.ts.mark(result1, "Status code is correct")

        result2 = self.api.validateResponseVsSchema(response.json())
        self.ts.markFinal(request.node.name, result2, "Schema is valid")

    # UPDATE
    def test_update_todo(self, request, todo_id, updated_todo):
        response = self.api.updateTodo(todo_id, updated_todo)

        result1 = self.api.verifyStatusCode(response.status_code, StatusCode.OK)
        self.ts.mark(result1, "Status code is correct")

        result2 = self.api.validateResponseVsSchema(response.json())
        self.ts.markFinal(request.node.name, result2, "Schema is valid")

    #  DELETE
    def test_remove_todo(self, request, todo_id):
        response = self.api.deleteTodo(todo_id)

        result1 = self.api.verifyStatusCode(response.status_code, StatusCode.OK)
        self.ts.mark(result1, "Status code is correct")

        result2 = self.api.validateResponseVsSchema(response.json())
        self.ts.markFinal(request.node.name, result2, "Schema is valid")