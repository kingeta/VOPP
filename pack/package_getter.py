"""Send Items and Box to paccurate API to return Packages"""
import requests, json
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
        concatenate = '''{"itemSets": ['''
        for item in items:
            item_string = '''{
                "refId": %s,
                "dimensions": {"x": %s, "y": %s, "z": %s},
                "quantity": %s
            },''' % (str(item.ref_id), str(item.dimensions[0]), str(item.dimensions[1]), str(item.dimensions[2]), str(item.quantity))
            concatenate += item_string
        concatenate = concatenate[:-1]
        concatenate += '''],'''
        box_string = '''
        "boxTypes": [{
            "weightMax": %s,
            "name": %s,
            "dimensions": {"x": %s, "y": %s, "z": %s}
        }]
        }''' % (str(box.max_weight), str(box.name), str(box.dimensions[0]), str(box.dimensions[1]), str(box.dimensions[2]))
        concatenate += box_string
        self.payload = json.dumps(concatenate)

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
        
