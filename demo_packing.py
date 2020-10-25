from package_getter import Packer
from warehouse import ItemSet, Box


# Set api key
API_KEY = 'PVjuMKCNFDZcPKdSJgeH_zun3r2ZAAiU-cXk0TClmc-zEUCogYBbvbepucZV8T3z'

# Create dummy data - "Four items, two boxes" — example 3 at docs.paccurate.io
items = [ItemSet((5, 6, 4), 2, 0, 4)]

# Specify types of boxes to be used — only one type in this case
boxes = [Box("5x6x8", (5, 6, 8), 150)]

# Pack stuff
WarehousePacker = Packer()
WarehousePacker.set_api_key(API_KEY)
packages = WarehousePacker.pack(items, boxes)

# Print packages
for package in packages:
  for itemset_and_location in package.itemsets_and_locations:
    # Print itemset (of only 1 item)
    print(itemset_and_location[0])
    # Print its location within Package Box
    print(itemset_and_location[1])
    print('\n')
  print(package)
  print('\n\n\n')

# Export images into html files into the pack/demos directory
# The images are identical in this example, try chaning items and boxes to see changes
with open('demo_image_1.html', 'w') as open_image_1, open('demo_image_2.html', 'w') as open_image_2:
    open_image_1.write(packages[0].image)
    open_image_2.write(packages[1].image)
