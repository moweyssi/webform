import yaml
from yaml import SafeLoader
import toml
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)
print(config)
print (toml.load("secrets.toml"))