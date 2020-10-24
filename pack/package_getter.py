"""Send Items and Box to paccurate API to return Packages"""
import requests
from .. import warehouse


class Packer:
    """Returning list of packages"""
    def __init__(self):
        self.payload = None
        self.headers = None

    def set_api_key(self, key):
        self.headers = None  # TODO

    def get_payload(self, items, box):
        pass

    def get_package(self, payload):
        pass
