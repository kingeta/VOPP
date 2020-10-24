"""Send Items and Box to paccurate API to return Packages"""
import requests
from .. import warehouse


class Packer:
    """Returning list of packages using the Paccurate API"""
    def __init__(self):
        self.payload = None
        self.headers = None
        self.response = None
        self.url = 'https://api.paccurate.io/'

    def set_api_key(self, key):
        api_key_value = f'apikey {key}'
        self.headers = {'Authorization': api_key_value}

    def get_payload(self, items, box):
        pass

    def get_response(self):
        if self.url is None:
            raise ValueError('The Paccurate API URL is not set')
        if self.payload is None:
            raise ValueError('There is no payload to send to the Paccurate API')
        if self.headers is None:
            raise ValueError('The Paccurate API key is not set')
        self.response = requests.post(self.url, data=self.payload, headers=self.headers)
        
    def get_package(self):
        if self.response is None:
            raise ValueError('There is no response from the Paccurate API')
        
