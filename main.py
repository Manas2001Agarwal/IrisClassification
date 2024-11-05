import os
import sys
from src.iris.components.data_ingestion import DataIngestion
from src.iris.config.configuration import ConfigurationEntity
from src.iris.components.data_validation import DataValidation


if __name__ == "__main__":
    configuration_manager = ConfigurationEntity()
    
    data_ingestion_config = configuration_manager.get_data_ingestion_config()
    data_ingestion = DataIngestion()
    data_ingestion.download_data(data_ingestion_config)
    
    data_validation_config = configuration_manager.get_data_validation_config()
    data_validation = DataValidation()
    data_validation.validate(data_validation_config)