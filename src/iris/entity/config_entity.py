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
    
@dataclass
class DataTransformationConfig:
    root_dir: Path
    source_file: Path
    test_file_name: Path
    train_file_name: Path
    preprocessor_file_path: Path
    
@dataclass
class ModelTrainerConfig:
    root_dir: Path
    source_train_file: Path
    source_test_file: Path
    model_file_path: Path
    params: dict