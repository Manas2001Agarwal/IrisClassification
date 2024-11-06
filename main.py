import os
import sys
from src.iris.components.data_ingestion import DataIngestion
from src.iris.config.configuration import ConfigurationEntity
from src.iris.components.data_validation import DataValidation
from src.iris.components.data_transformation import DataTransformation
from src.iris.components.model_trainer import ModelTrainer

if __name__ == "__main__":
    configuration_manager = ConfigurationEntity()
    
    data_ingestion_config = configuration_manager.get_data_ingestion_config()
    data_ingestion = DataIngestion()
    data_ingestion.download_data(data_ingestion_config)
    
    data_validation_config = configuration_manager.get_data_validation_config()
    data_validation = DataValidation()
    data_validation.validate(data_validation_config)
    
    data_transformation_config = configuration_manager.get_data_transformation_config()
    data_transformation = DataTransformation()
    data_transformation.transform_data(data_transformation_config)
    
    model_trainer_config = configuration_manager.get_model_trainer_config()
    model_trainer = ModelTrainer(model_trainer_config)
    accu,report = model_trainer.train_evaluate_model()
    
    print(accu)
    print(report)
    