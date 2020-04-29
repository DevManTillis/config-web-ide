#!/usr/bin/env python3
from flask import Flask, render_template
from flask import request, redirect
from flask import jsonify
import json
import yaml
from collections import OrderedDict
from webtemplates import CSS,NAV
from uisources import YamlMods
import uuid
import pymongo
import datetime


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)

# connection = Connection()

# @connection.register
# class BlogPost(Document):
#     __database__ = 'test'
#     __collection__ = 'example'
#     skeleton = {
#             'title':unicode,
#             'body':unicode,
#             'author':unicode,
#             'date_creation':datetime.datetime,
#             'rank':int
#     }
#     optional = {
#             'tags': [unicode],
#     }
#     default_values = {'rank':0, 'date_creation':datetime.datetime.utcnow}
# blogpost = con.BlogPost()


# app = Flask(__name__, template_folder="/home/sysadmin/configurator-web-ide/templates")

# @app.route("/config_sets")
# def get_config_set():
#     return jsonify(CONFIG_SET)


# @app.route("/modify_config_set")
# def post_config_set():
#     return jsonify(CONFIG_SET)


# if __name__ == "__main__":
#     app.run(debug=True, host='0.0.0.0')
# #  We made two new changes