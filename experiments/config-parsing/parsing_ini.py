import configparser
import os

config = configparser.ConfigParser()
config_file_path = os.path.join(os.path.dirname(__file__), 'config.ini')

config.read(config_file_path)

# {'section' : {key:value, key1, value1}}
# for every section 
#   unpack the keys and values into enventries with the current section name

for section in config.sections():
    print(section) # database, server, etc/

    for key, value in config.items(section):
        print(key, value) # host, localhost, etc.
