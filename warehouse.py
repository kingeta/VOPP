"""Classes used in warehouse"""


class ItemSet():
    """A set of identical items.
    
    The dimensions x, y, z are the dimensions of a single item.
    The weight is a weight of a single member"""
    def __init__(self, x, y, z, weight, ref_id, quantity = 1):
        self.x = x
        self.y = y
        self.z = z
        self.weight = weight
        self.ref_id = ref_id
        self.quantity = quantity
    
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z}), {self.weight}"


class Box():
    def __init__(self, x, y, z):
        pass


class Package():
    pass
