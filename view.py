#!/usr/bin/env python3
from flask import Flask, render_template
from flask import request, redirect
from flask import jsonify
import json
import yaml
from uisources import YamlMods
from collections import OrderedDict
from webtemplates import CSS,NAV
import uuid


app = Flask(__name__, template_folder="webtemplates")


@app.route("/")
def config_sets():
    return render_template("index.html")


@app.route("/playbooks")
def playbooks():
    return render_template("playbooks.html")


@app.route("/inventory")
def inventory():
    return render_template("inventory.html")


@app.route("/ansible_cfg")
def ansible_cfg():
    return render_template("ansible_cfg.html")


@app.route("/logs")
def logs():
    return render_template("logs.html")


@app.route("/python_libs")
def python_libs():
    return render_template("python_libs.html")


@app.route("/roles")
def roles():
    return render_template("roles.html")


@app.route("/edit_playbook")
def edit_playbook():
    return render_template("edit_playbook.html")


@app.route('/submit', methods = ['POST'])
def submit():
    yaml_data = request.form['yaml_data']
    yaml_mod  = YamlMods()
    JSON      = yaml_mod.validateYaml(yaml_data)

    if yaml_mod.validated:
        YAML = yaml.dump(JSON, default_flow_style=False, Dumper=yaml_mod.dumper, sort_keys=False)
        print(YAML)
        print(JSON)
        yaml_file = open(f"playbooks/{uuid.uuid4()}.yml","w")
        yaml_file.write(YAML)
        yaml_file.close()
    else:
        print({"result":False, "data": [f"validation error: {JSON}"]})
    return render_template("index.html", messages={"response": JSON})
    #return redirect('/')

    

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
