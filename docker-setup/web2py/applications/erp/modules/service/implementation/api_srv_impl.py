from gluon import current
from service.interface.api_srv import APIService
import requests
import yaml, cPickle

class APIServiceImplementation(APIService):
    def __init__(self):
        self.host = "http://api/api/v1"

    def get(self, uri, payload):
        """
        Sends uri concatenated with payloads to api_service.

        Does not communicate directly with dao.
        Sends requests to api_service.
        Gets response from api_service with serialized data.
        Deserializes response using cPickle.
        """
        curr_host = "http://"+uri.split("/")[1]+"/api/v1"
        response = requests.get(curr_host+uri,payload)        
        response_dict = yaml.safe_load(response.content)
        response_data = cPickle.loads(response_dict["data"])     
        return response_data
    
    def post(self, uri, payload):
        curr_host = "http://"+uri.split("/")[1]+"/api/v1"
        response = requests.get(curr_host+uri,payload)        
        response_dict = yaml.safe_load(response.content)
        response_data = cPickle.loads(response_dict["data"])     
        return response_data