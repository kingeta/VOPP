"""Classes used in warehouse"""


class Item():
    def __init__(self, x, y, z, weight, id):
        self.x = x
        self.y = y
        self.z = z
        self.weight = weight
        self.id = id


class Box():
    def __init__(self, x, y, z):
        pass


class Package():
    pass
