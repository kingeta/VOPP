# VOPP - Virtual Operation Process Planning

## What is VOPP?
[VOPP](https://github.com/kingeta/VOPP) is Python-based library that improves the logistics of warehouses and businesses that exchange packages and physical goods between each other. VOPP reduces costs associated with package management by improving packaging efficiency whilst also reducing the number of errors made in the process. It is a fully integrated end-to-end solution that provides a complete loop for warehouses and their customers and contractors to optimize their logistics.

## Why should our business use VOPP?
VOPP is a Free-and-Open-Source package licensed under the [MIT License](https://github.com/kingeta/VOPP/blob/main/LICENSE), so it is ideal for SMEs that want to reduce their logistics costs without paying for an expensive commercial solution. VOPP is completely modular and flexible, consisting of multiple interconnected components that can be used for other parts of the business and hence connect to existing solutions in a non-disruptive manner. Furthermore, the intuitive UI of the VOPP web app is very easy to use and doesn't require the employees to endure a steep learning curve. 

## How does VOPP work?
At the beginning of the VOPP cycle there is a _Customer_, for example a Store that wants to order a product consisting of multiple parts located in a _Warehouse_. The _Customer_ opens the online web application and inputs the IDs of items that they require.

The item IDs are then sent to the _Warehouse_, where they are used to find the actual _Items_ in the database of all parts and retrieved along with their properties. The _Warehouse_ then selects the _Boxes_ that they have available for packing.

These items and boxes are then send to the [Paccurate API](https://paccurate.io/), which returns a list of _Packages_, where each package corresponds to a _Box_ of efficiently packed _Items_. These are returned along with instructions of packing order and also an image to graphically aid the packing.

This information is displayed on the web application in a warehouse computer to a warehouse employee, who finds each _Item_ in the warehouse, scans its barcode with a barcode scanner as a proof of it being packed, and places it into the _Box_ in the required order.

Once this is completed, the _Package_ is shipped to the _Customer_.

When the _Package_ arrives, the _Customer_ opens the web application again, where another interactive interface is waiting. Here, they can tick off every item that should have been delivered, and in the unfortanet event of an item being lost in delivery, the _Customer_ doesnt tick that item off, and the web app automatically suggests another _Order_ to the _Warehouse_.

This completes the end-to-end loop of VOSS, which completes all the logistics between the _Customer_ and the _Warehouse_.

## How should we run VOPP?
explain the tech stack

## TODOs
- [ ] Remove TODOs
- [ ] Finalize file-directory structure (interfacing of modules)
- [ ] Remove legacy files and directories (pack???)
- [ ] Finalize code style
- [ ] Add license
- [ ] Write docstrings
- [ ] Come up with fancy name???
- [ ] Create `requirements.txt`
- [ ] Write instalation and running instructions into README
- [ ] Add examples (gifs) and documentation into README
