import os
import yaml


class ConfigUtils(object):
    _instance = None
    props: dict

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigUtils, cls).__new__(cls)
            parent_module = os.path.join(*(cls.__module__.split('.')[:-1]))
            parent_module_path = os.path.abspath(parent_module).split("fipomdp")[0] + "fipomdp"
            yaml_path = os.path.join(parent_module_path, "config", "experiment_config.yaml")
            cls._instance._load_yaml(yaml_path)
        return cls._instance

    def get_config_property(self, config_property):
        return self.props[config_property]

    def set_config_property(self, config_property, value):
        self.props[config_property] = value

    def _load_yaml(self, filepath):
        with open(filepath, "r") as stream:
            self.props = yaml.safe_load(stream)
