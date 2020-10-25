"""Module for sending Items and Boxes to Paccurate API to return Packages"""
import requests
import json


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

    def get_payload(self, items, box):  # Deprecated TODO Delete
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
    
    def set_payload(self, items, boxes):
        """Items is a list of class ItemSet objects and boxes is a list of class Box objects"""
        itemsets = list()
        for itemset in items:
            itemset_dimensions = dict(x=itemset.dimensions[0],
                                      y=itemset.dimensions[1],
                                      z=itemset.dimensions[2])
            itemsets.append(dict(refId=itemset.ref_id,
                                 weight=itemset.weight,
                                 dimensions=itemset_dimensions,
                                 quantity=itemset.quantity))
        boxtypes = list()
        for box in boxes:
            box_dimensions = dict(x=box.dimensions[0],
                                  y=box.dimensions[1],
                                  z=box.dimensions[2])
            boxtypes.append(dict(weightMax=box.max_weight,
                                 name=box.name,
                                 dimensions=box_dimensions))

        payload = dict(itemSets=itemsets,
                       boxTypes=boxtypes)
        self.payload = json.dumps(payload)


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
        # TODO
        # return json.loads(self.response.text)
