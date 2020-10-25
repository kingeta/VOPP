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
        return f"An ItemSet of {self.quantity} individual items of size {self.dimensions}, individual weight {self.weight}, id {self.ref_id}"


class Box:
    """A Box dimensions is a tuple of (x, y, z)"""
    def __init__(self, name, dimensions, max_weight):
        self.name = name
        self.dimensions = dimensions
        self.max_weight = max_weight
    
    def __str__(self):
        return f'A {self.name} Box of size {self.dimensions} and maximum weight {self.max_weight}'


class Package:
    """A Package corresponds to one Box that contains
    items of class ItemSet of quantity 1.
    itemsets_and_locations is a list of tuples ordered by the order of packages being put in the box
    each tuple contains a ItemSet class and a """
    def __init__(self, itemsets_and_locations, box, image):
        self.itemsets_and_locations = itemsets_and_locations
        self.box = box
        self.image = image

    def __str__(self):
        return f'Package of Box {self.box} containing ItemSets at locations {self.itemsets_and_locations}'
