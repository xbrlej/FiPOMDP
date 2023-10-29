import os
import yaml

class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


class ConfigUtils(Singleton):
    props: dict

    def __init__(self):
        parent_module = os.path.join(*(self.__module__.split('.')[:-1]))
        parent_module_path = os.path.abspath(parent_module).split("fipomdp")[0] + "fipomdp"
        yaml_path = os.path.join(parent_module_path, "config", "experiment_config.yaml")
        self._load_yaml(yaml_path)

    def get_config_property(self, config_property):
        return self.props[config_property]

    def _load_yaml(self, filepath):
        with open(filepath, "r") as stream:
            self.props = yaml.safe_load(stream)
