from pathlib import Path
import os, sys
import yaml
from box import ConfigBox

def read_yaml(path:Path) -> ConfigBox:
    print(path)
    content = yaml.safe_load(open(path,"r"))
    return ConfigBox(content)