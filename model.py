#!/usr/bin/env python3
from flask import Flask, render_template
from flask import request, redirect
from flask import jsonify
import json
import yaml
from collections import OrderedDict
from templates import CSS,NAV
from uisources import YamlMods
import uuid


app = Flask(__name__, template_folder="/home/sysadmin/configurator-web-ide/templates")


CONFIG_SET_TABLE = {
    "result": True,
    "message": {
        "config_sets": [{
            "config_set_id"  : int(),  # Primary Key
            "ansible_params" : str(),  # Parameters to supply to ansible-playbook
            "playbooks"      : bool(), # 1:M
            "inventory"      : bool(), # 1:M
            "logs"           : bool(), # 1:M
            "roles"          : bool(), # 1:M
            "ansible_cfg"    : bool()
        }]
    }
}


PLAYBOOKS_TABLE = {
    "result": True,
    "message": {
        "playbooks": [{
            "config_set_id" : int(), # Primary Key - 1:M Relationship w/ config set
            "playbook_yaml" : OrderedDict()
            }]
    }
}


CONFIG_SET = {
    "result": True,
    "message": {
        "config_sets": [{
            "config_set_id"  : int(),  # Primary Key
            "ansible_params" : str(),  # Parameters to supply to ansible-playbook
            "playbooks"      : bool(), # 1:M
            "inventory"      : bool(), # 1:M
            "logs"           : bool(), # 1:M
            "roles"          : bool(), # 1:M
            "ansible_cfg"    : bool()
        }]
    }
}


PLAYBOOKS = {
    "result": True,
    "message": {
        "playbooks": [{
            "config_set_id" : int(), # Primary Key - 1:M Relationship w/ config set
            "playbook_yaml" : OrderedDict()
            }]
    }
}


@app.route("/config_sets")
def get_config_set():
    return jsonify(CONFIG_SET)


@app.route("/modify_config_set")
def post_config_set():
    return jsonify(CONFIG_SET)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
#  We made two new changes