from flask import Flask, render_template, request, redirect, url_for, make_response
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from .. import warehouse 
#import mistune

mongo_uri = "mongodb://localhost:27017/VOPP"

app = Flask(__name__)
app.config['Mongo_URI'] = mongo_uri
mongo = PyMongo(app, uri = mongo_uri)

@app.route('/test')
def test():
    inputs = "0\n1"
    items = list(map(int, inputs.split("\n")))
    obj_list = []
    for i in items:
        i_params = mongo.db['inventory'].find()[i]
        obj_list.append(warehouse.ItemSet(i_params['x'],i_params['y'],i_params['z'],i_params['weight'],i))
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
    return "Shipping"

@app.route('/receiving')
def receiving():
    return "Receiving"
