import requests
import utilities.custom_logger as cl
from utilities.util import Util
from traceback import print_stack
import jsonschema

class ApiClient(requests.Session):
    log = cl.customLogger()

    def __init__(self, api_name):
        super(ApiClient, self).__init__()
        self.hooks['response'].append(self.log_details)
        self.url = ''
        self.util = Util()

    def log_details(self, response, *args, **kwargs):
        self.log.info("Request {}: {}".format(response.request.method, response.request.url))
        self.log.info("Request Headers: {}".format(response.request.headers))
        if response.request.body is not None:
            self.log.info("Request Body: {}".format(response.request.body))

        self.log.info("Response Status: {}, elapsed: {}s".format(response.status_code, response.elapsed.total_seconds()))
        self.log.info("Response Headers: {}".format(response.headers))
        if response.text != "":
            self.log.info("Response Body: {}".format(response.text))

        self.url = 'https://jsonplaceholder.typicode.com/users'

    def read_all(self):
        self.log.info("READ ALL request")
        return self.get(self.url)

    def read(self, _id):
        self.log.info("READ request")
        return self.get(self.url + '/' + str(_id))

    def create(self, _new_data):
        self.log.info("CREATE request")
        return self.post(self.url, json=_new_data)

    def update(self, _id, _updated_data):
        self.log.info("UPDATE request")
        return self.put(self.url + '/' + str(_id), _updated_data)

    def remove(self, _id):
        self.log.info("DELETE request")
        return self.delete(self.url + '/' + str(_id))

    def verifyStatusCode(self, actualStatusCode, expectedStatusCode):
        try:
            return self.util.verifyNumbersMatch(actualStatusCode, expectedStatusCode)
        except:
            self.log.error("Failed to get status code")
            print_stack()
            return False

    def validateJsonResponseVsSchema(self, jsonResponce, schema={}):
         return jsonschema.Draft3Validator(schema).is_valid(jsonResponce)