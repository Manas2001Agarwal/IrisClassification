from dataclasses import dataclass
import os
import sys
from pathlib import Path
from box import ConfigBox

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_file: str
    raw_data_file_path: Path
    
@dataclass
class DataValidationConfig:
    root_dir: Path
    status_file_name: Path
    source_file: Path
    schema: dict
    
