#!/usr/bin/env python3
from flask import Flask, render_template
from flask import request, redirect
from flask import jsonify
import json
import yaml
from collections import OrderedDict
from templates import CSS,NAV
import uuid


app = Flask(__name__, template_folder="/home/sysadmin/configurator-web-ide/templates")


class MyDumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super(MyDumper, self).increase_indent(flow, False)


class YamlMods:
    @property
    def dumper(self):
        return MyDumper

    @property
    def validated(self):
        return self.validate

    def validateYaml(self, config):
        try:
            config = yaml.load(config, Loader=yaml.SafeLoader)
            self.validate = True
            return config
        except Exception as err:
            self.validate = False
            return err


@app.route("/")
def home():
    return render_template("index.html")


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
#  We made two new changes