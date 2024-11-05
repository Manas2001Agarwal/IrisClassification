from dataclasses import dataclass
import os
import sys
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_file: str
    raw_data_file_path: Path