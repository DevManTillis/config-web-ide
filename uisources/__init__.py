import yaml

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
            return {"result" : False, "message": str(err)}
