import sys
import os
import yaml
from pathlib import Path
from src.iris.entity.config_entity import (DataIngestionConfig,
                                           DataValidationConfig,
                                           DataTransformationConfig)
from src.iris.utils.common import read_yaml
from src.iris.constants import (CONFIG_FILE_PATH,
                                PARAMS_FILE_PATH,
                                SCHEMA_FILE_PATH)

class ConfigurationEntity:
    def __init__(self):
        self.config = read_yaml(path=CONFIG_FILE_PATH)
        self.params = read_yaml(path=PARAMS_FILE_PATH)
        self.schema = read_yaml(path=SCHEMA_FILE_PATH)
        
        os.makedirs(self.config.artifacts_root,exist_ok=True)
        
    def get_data_ingestion_config(self):
        config = self.config.data_ingestion
        os.makedirs(config.root_dir,exist_ok=True)
        
        return DataIngestionConfig(
            root_dir=config.root_dir,
            source_file=config.source_file,
            raw_data_file_path=config.raw_data_file_path
        )
        
    def get_data_validation_config(self):
        config = self.config.data_validation
        os.makedirs(config.root_dir,exist_ok=True)
        
        return DataValidationConfig(
            root_dir=config.root_dir,
            status_file_name=config.status_file_name,
            source_file=config.source_file,
            schema = self.schema.COLUMNS
        )
        
    def get_data_transformation_config(self):
        config = self.config.data_transformation
        os.makedirs(config.root_dir,exist_ok=True)
        
        return DataTransformationConfig(
            root_dir= config.root_dir,
            source_file=config.source_file,
            test_file_name=config.test_file_name,
            train_file_name=config.train_file_name,
            preprocessor_file_path=config.preprocessor_file_path
        )
        
        