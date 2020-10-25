from os import path
from flask import Flask, render_template, request, redirect, url_for, make_response
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import sys
sys.path.append('..')
from warehouse import ItemSet, Box
from package_getter import Packer
#import mistune



mongo_uri = "mongodb://localhost:27017/VOPP"
template_path = path.abspath('VOPP_web/templates')

app = Flask(__name__, template_folder = template_path)
app.config['Mongo_URI'] = mongo_uri
#application = app.app
mongo = PyMongo(app, uri = mongo_uri)
obj_list = []
list_item_ids = []

def format_input(input_order):
    formatted = input_order.split("\n")
    for i in range(len(formatted)):
        formatted[i] = list(map(int, formatted[i].split(" ")))
    return formatted

# def format_input_2(input_order):
#     formatted = input_order.split('\n')
#     return {int(a): int(b) for a, b in map(lambda t: t.split(' '), formatted)}

@app.route('/test')
def test():
    obj_list.clear()
    inputs = "9780007466061 2\n5060181370243 1"
    # inputs = "0 2\n1 2"
    items = format_input(inputs)
    # app.logger.debug('items', items)
    # app.logger.debug(obj_list)
    
    for item, quantity in items:
        i_params = mongo.db['storage'].find({'item': item})[0] 
        obj_list.append(ItemSet((i_params['x']/5,i_params['y']/5,i_params['z']/5),i_params['weight'], item, quantity, i_params['color']))
    
    #return ', '.join(map(lambda t: str(t.x), obj_list))
    return "\r\n".join(map(str, obj_list))

@app.route('/')
def input():
    return render_template('input.jinja')
    

@app.route('/add', methods = ['POST'])
def input_read():
    input_text = request.form['text']
    app.logger.debug( input_text )

    return redirect(url_for('input'))

@app.route('/shipping')
def shipping():
    test()
    list_item_ids.clear()
    for it in obj_list:
        for _ in range(it.quantity):
            list_item_ids.append(str(it.ref_id))
    app.logger.debug(list_item_ids)
    return render_template('worker.jinja', items=list_item_ids) # list of ids as strings

@app.route('/shipping/addCheckBox', methods = ['POST'])
def checkbox_input():
    if request.method == 'POST':
        for part in request.form.getlist('parts'):
            print(part)
    
    return redirect(url_for('shipping'))

@app.route('/receiving')
def receiving():
    # Cribbed from the old demo file

    # Set api key
    API_KEY = 'PVjuMKCNFDZcPKdSJgeH_zun3r2ZAAiU-cXk0TClmc-zEUCogYBbvbepucZV8T3z'

    # Create dummy data , Four items, two boxes , example 3 at docs.paccurate.io
    # items = [ItemSet((5, 6, 4), 2, 0, 4)]
    test()
    items = obj_list
    # app.logger.debug(items)

    # Specify types of boxes to be used — only one type in this case
    boxes = [Box("5x6x8", (5, 6, 8), 150)]

    # Pack stuff
    WarehousePacker = Packer()
    WarehousePacker.set_api_key(API_KEY)
    packages = WarehousePacker.pack(items, boxes)

    # app.logger.debug(packages[0].image)

    return render_template('receiver.jinja', images = [p.image for p in packages])
