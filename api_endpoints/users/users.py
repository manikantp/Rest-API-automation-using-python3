from api_client.api_client import ApiClient
import utilities.custom_logger as cl
from schemas.users.users import schema_user, schema_users

class Users(ApiClient):
    log = cl.customLogger()

    def __init__(self):
        super(Users, self).__init__(self.__class__.__name__)
        self.url = 'https://jsonplaceholder.typicode.com/users'

    def createUser(self, newUser):
        return self.create(newUser)

    def readUser(self, _id):
        return self.read(_id)

    def updateUser(self, _id, updated_user):
        return self.update(_id, updated_user)

    def deleteUser(self, _id):
        return self.remove(_id)

    def validateResponseVsSchema(self, jsonResponce, schema=schema_user):
         return self.validateJsonResponseVsSchema(jsonResponce, schema)
