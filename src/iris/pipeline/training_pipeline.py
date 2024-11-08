import os
import sys
from src.iris.components.data_ingestion import DataIngestion
from src.iris.config.configuration import ConfigurationEntity
from src.iris.components.data_validation import DataValidation
from src.iris.components.data_transformation import DataTransformation
from src.iris.components.model_trainer import ModelTrainer

class Training_Pipeline:
    def __init__(self):
        self.configuration_manager = ConfigurationEntity()
        
    def initiate_data_ingestion(self):
        data_ingestion_config = self.configuration_manager.get_data_ingestion_config()
        data_ingestion = DataIngestion()
        data_ingestion.download_data(data_ingestion_config)
        
    def initiate_data_validation(self):
        data_validation_config = self.configuration_manager.get_data_validation_config()
        data_validation = DataValidation()
        data_validation.validate(data_validation_config)
        
    def initiate_data_transformation(self):
        data_transformation_config = self.configuration_manager.get_data_transformation_config()
        data_transformation = DataTransformation()
        data_transformation.transform_data(data_transformation_config)
        
    def initiate_model_training(self):
        model_trainer_config = self.configuration_manager.get_model_trainer_config()
        model_trainer = ModelTrainer(model_trainer_config)
        accu,report = model_trainer.train_evaluate_model()
        return accu,report
    
    def run_training_pipeline(self):
        self.initiate_data_ingestion()
        self.initiate_data_validation()
        self.initiate_data_transformation()
        accu,report = self.initiate_model_training()
        
        return accu,report