from flask import Flask, render_template, request, redirect, url_for, make_response
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
#import mistune

mongo_uri = "mongodb://localhost:27017/VOPP"

app = Flask(__name__)
app.config['Mongo_URI'] = mongo_uri
mongo = PyMongo(app, uri = mongo_uri)

class item():
    def __init__(self, x, y, z, weight, id):
        self.x = x
        self.y = y
        self.z = z
        self.weight = weight
        self.id = id

@app.route('/')
def input():
    return render_template('input.jinja')

@app.route('/add', methods = ['POST'])
def input_read():
    input_text = request.form['text']
    app.logger.debug( input_text )

    return redirect( url_for('input') )