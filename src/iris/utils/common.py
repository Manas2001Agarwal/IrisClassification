from pathlib import Path
import os, sys
import yaml

from dotmap import DotMap

def read_yaml(path:Path) -> DotMap:
    content = yaml.safe_load(open(path,"r"))
    return DotMap(content)

