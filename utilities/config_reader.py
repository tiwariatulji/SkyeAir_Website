from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

def get_config(section, key):
    return config.get(section, key)
