import os

from bson.objectid import ObjectId
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'kevin'
app.config['MONGO_URI'] = os.getenv('MONGO_URI', 'mongodb://localhost')
mongo = PyMongo(app)

@app.route('/')
def hello():
    return "Hello, World"

@app.route('/show/<id>')
def show(id):
    info = mongo.db.users.find_one({'_id': ObjectId(id)})
    return info["username"]

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=5000),
            debug=True)