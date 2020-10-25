import json
# This script is Deprecated TODO Delete
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
        return f"({self.dimensions}), {self.weight}"
class Box:
    """ dimensions is a tuple of (x, y, z)"""
    def __init__(self, name, dimensions, max_weight):
        self.name = name
        self.dimensions = dimensions
        self.max_weight = max_weight

obj_list = []
obj_list.append(ItemSet((1,1,1), 5, 0, 2))
obj_list.append(ItemSet((2,2,2), 10, 1, 1))

box0 = Box("5x6x8", (5, 6, 8), 150)

def get_payload(items, box):
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
    payload = json.dumps(concatenate)
    return payload

print(get_payload(obj_list, box0))
