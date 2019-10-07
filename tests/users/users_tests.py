import pytest
from api_endpoints.users.users import Users
from utilities.teststatus import TestStatus
import utilities.constants.status_codes as StatusCode

class TestUsers():

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.api = Users()
        self.ts = TestStatus()

    @pytest.fixture
    def user_id(self):
        return 1

    @pytest.fixture
    def new_user(self):
        return {
            "name": "Leanne Graham",
            "username": "Bret",
            "email": "Sincere@april.biz",
            "address": {
                "street": "Kulas Light",
                "suite": "Apt. 556",
                "city": "Gwenborough",
                "zipcode": "92998-3874",
                "geo": {
                    "lat": "-37.3159",
                    "lng": "81.1496"
                }
            },
            "phone": "1-770-736-8031 x56442",
            "website": "hildegard.org",
            "company": {
                "name": "Romaguera-Crona",
                "catchPhrase": "Multi-layered client-server neural-net",
                "bs": "harness real-time e-markets"
            }
        }


    @pytest.fixture
    def updated_user(self):
        return {
          "name": "Ervin Howell",
          "username": "Antonette",
          "email": "Shanna@melissa.tv",
          "address": {
            "street": "Victor Plains",
            "suite": "Suite 879",
            "city": "Wisokyburgh",
            "zipcode": "90566-7771",
            "geo": {
              "lat": "-43.9509",
              "lng": "-34.4618"
            }
          },
          "phone": "010-692-6593 x09125",
          "website": "anastasia.net",
          "company": {
            "name": "Deckow-Crist",
            "catchPhrase": "Proactive didactic contingency",
            "bs": "synergize scalable supply-chains"
          }
        }

    # CRUD operations
    # CREATE
    def test_create_user(self, request, new_user):
        response = self.api.createUser(new_user)
        result1 = self.api.verifyStatusCode(response.status_code, StatusCode.CREATED)
        self.ts.mark(result1, "Status code is correct")

        result2 = self.api.validateResponseVsSchema(response.json())
        self.ts.markFinal(request.node.name, result2, "Schema is valid")


    #  READ
    def test_read_one_user(self, request, user_id):
        response = self.api.readUser(user_id)

        result1 = self.api.verifyStatusCode(response.status_code, StatusCode.OK)
        self.ts.mark(result1, "Status code is correct")

        result2 = self.api.validateResponseVsSchema(response.json())
        self.ts.markFinal(request.node.name, result2, "Schema is valid")

    # UPDATE
    def test_update_user(self, request, user_id, updated_user):
        response = self.api.updateUser(user_id, updated_user)

        result1 = self.api.verifyStatusCode(response.status_code, StatusCode.OK)
        self.ts.mark(result1, "Status code is correct")

        result2 = self.api.validateResponseVsSchema(response.json())
        self.ts.markFinal(request.node.name, result2, "Schema is valid")

    #  DELETE
    def test_remove_user(self, request, user_id):
        response = self.api.deleteUser(user_id)

        result1 = self.api.verifyStatusCode(response.status_code, StatusCode.OK)
        self.ts.mark(result1, "Status code is correct")

        result2 = self.api.validateResponseVsSchema(response.json())
        self.ts.markFinal(request.node.name, result2, "Schema is valid")
