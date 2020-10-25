from flask import Flask, render_template, request, redirect, url_for, make_response
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from .. import warehouse 
#import mistune

mongo_uri = "mongodb://localhost:27017/VOPP"

app = Flask(__name__)
app.config['Mongo_URI'] = mongo_uri
mongo = PyMongo(app, uri = mongo_uri)

def format_input(input_order):
    formatted = input_order.split("\n")
    for i in range(len(formatted)):
        formatted[i] = list(map(int, formatted[i].split(" ")))
    return formatted

@app.route('/test')
def test():
    inputs = "0 2\n1 1"
    items = format_input(inputs)
    obj_list = []
    app.logger.debug(obj_list)
    for item_id in items:
        i_params = mongo.db['inventory'].find()[item_id[0]]
        obj_list.append(warehouse.ItemSet((i_params['x'],i_params['y'],i_params['z']),i_params['weight'],item_id[0], item_id[1]))
    app.logger.debug(obj_list)
    #return ', '.join(map(lambda t: str(t.x), obj_list))
    return "\r\n".join(map(str, obj_list))

@app.route('/')
def input():
    return render_template('input.jinja')
    

@app.route('/add', methods = ['POST'])
def input_read():
    input_text = request.form['text']
    app.logger.debug( input_text )

    return redirect( url_for('input') )

@app.route('/shipping')
def shipping():
    return render_template('worker.jinja')

@app.route('/shipping/addCheckBox', methods = ['POST'])
def checkbox_input():
    if request.method == 'POST':
        for part in request.form.getlist('parts'):
            print(part)
    
    return redirect( url_for('shipping') )

@app.route('/receiving')
def receiving():
    return render_template('receiver.jinja')
