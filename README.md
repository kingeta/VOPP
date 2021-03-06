# VOPP - Virtual Operation Process Planning

![VOPP](https://github.com/kingeta/VOPP/raw/main/pack/images/vopp.PNG)

## What is VOPP?
[VOPP](https://github.com/kingeta/VOPP) is Python-based library that improves the logistics of warehouses and businesses that exchange packages and physical goods between each other. VOPP reduces costs associated with package management by improving packaging efficiency whilst also reducing the number of errors made in the process. It is a fully integrated end-to-end solution that provides a complete loop for warehouses and their customers and contractors to optimize their logistics.

## Why should our business use VOPP?
The majority of VOPP is Free-and-Open-Source and licensed under the [MIT License](https://github.com/kingeta/VOPP/blob/main/LICENSE), so it is ideal for SMEs that want to reduce their logistics costs without paying for an expensive commercial solution. VOPP is completely modular and flexible, consisting of multiple interconnected components that can be used for other parts of the business and hence connect to existing solutions in a non-disruptive manner. Furthermore, the intuitive UI of the VOPP web app is very easy to use and doesn't require the employees to endure a steep learning curve. 

## How does VOPP work?
At the beginning of the VOPP cycle there is a _Customer_, for example a Store that wants to order a product consisting of multiple parts located in a _Warehouse_. The _Customer_ opens the online web application and inputs the IDs of items that they require.

![Customer_Order](https://github.com/kingeta/VOPP/raw/main/pack/images/Capture_input_order.PNG)

The item IDs are then sent to the _Warehouse_, where they are used to find the actual _Items_ in the database of all parts and retrieved along with their properties. The _Warehouse_ then selects the _Boxes_ that they have available for packing.

These items and boxes are then send to the [Paccurate API](https://paccurate.io/), which returns a list of _Packages_, where each package corresponds to a _Box_ of efficiently packed _Items_. These are returned along with instructions of packing order and also an image to graphically aid the packing.

![Packing](https://github.com/kingeta/VOPP/raw/main/pack/images/Capture_shipping_worker.PNG)

This information is displayed on the web application in a warehouse computer to a warehouse employee, who finds each _Item_ in the warehouse, scans its barcode with a barcode scanner as a proof of it being packed, and places it into the _Box_ in the required order.

![Barcode Scanning](https://github.com/kingeta/VOPP/raw/main/pack/images/scanning_barcode.png)

Once this is completed, the _Package_ is shipped to the _Customer_.

When the _Package_ arrives, the _Customer_ opens the web application again, where another interactive interface is waiting. Here, they can tick off every item that should have been delivered.

![Order Arrived](https://github.com/kingeta/VOPP/raw/main/pack/images/Capture_receiver_end.PNG)

In the unfortanet event of an item being lost in delivery, the _Customer_ doesnt tick that item off, and the web app automatically suggests another _Order_ to the _Warehouse_.

![Refund](https://github.com/kingeta/VOPP/raw/main/pack/images/Capture_refund.PNG)

This completes the end-to-end loop of VOSS, which completes all the logistics between the _Customer_ and the _Warehouse_.

## How does VOPP work under the hood?
Under the Hood, VOPP consists of multiple interconnected modular components.

![Tech_Stack](https://github.com/kingeta/VOPP/raw/main/pack/images/tech_stack.png)

The web app runs on Flask, which interfaces the _Warehouse_, which consists of a MongoDB database for the items. Once the queried items are retrieved from the database, they are bundled into _ItemSets_ and send alongside with _Boxes_ to the _Packer_ class. _Packer_ sends a HTTP post request to Paccurate API. The repsponse from the API is parsed and converted into a list of _Packages_. These are then displayed in the web app. The web app is then connected the the barcode scanner, which inputs the data.

All other components just use the Flask app.

## Authors
**The Bowden Cables** Team of the IfM Hackathon 2020.
- Herby Bowden (capt'n)
- Egle Augustaityte
- Louis Relandeau
- David O'Brien-Moller
- Adam Sroka
