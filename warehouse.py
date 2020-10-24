"""Classes used in warehouse"""


class ItemSet:
    """A set of identical items.
    
    The dimensions is a tuple (x, y, z) of the dimensions of a single item.
    The weight is a weight of a single member"""
    def __init__(self, dimensions, weight, ref_id, quantity):
        self.dimensions = dimensions
        self.weight = weight
        self.ref_id = ref_id
        self.quantity = quantity
    
    def __str__(self):
        return f"{self.dimensions},{self.weight}"


class Box:
    """ dimensions is a tuple of (x, y, z)"""
    def __init__(self, name, dimensions, max_weight):
        self.name = name
        self.dimensions = dimensions
        self.max_weight = max_weight


class Package:
    """A package corresponds to one box.
    items of class ItemSet of quantity 1, packed in a box of class Box
    items is a list of tuples ordered by the order of packages being put in the box
    each tuple contains a ItemSet class and a """
    def __init__(self, items, box, image):
        self.items = items
        self.box = box
        self.image = image
