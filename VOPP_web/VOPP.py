from flask import Flask, render_template, request, redirect, url_for, make_response
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
#import mistune

mongo_uri = "mongodb://localhost:27017/VOPP"

app = Flask(__name__)
app.config['Mongo_URI'] = mongo_uri
mongo = PyMongo(app, uri = mongo_uri)


@app.route('/')
def home():
    return "Now THIS is a website"