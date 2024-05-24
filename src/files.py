import yaml
from yaml.error import YAMLError

ARCHIVES_FOLDER = "./archives"
DATA_FOLDER = f"{ARCHIVES_FOLDER}/data"
TARGET_FOLDER = f"{ARCHIVES_FOLDER}/target"


def read_config(path:str):
    try:
        with open(path, "r") as f:
            ##print('deuboa') 
            return yaml.safe_load(f)
    except YAMLError as e:
        print(e)


def read_schema(path:str):
    with open(path, "r") as f: 
        schema = f.read()        
        return schema

