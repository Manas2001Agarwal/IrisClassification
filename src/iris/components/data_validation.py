from src.iris.entity.config_entity import DataValidationConfig
from src.iris.config.configuration import ConfigurationEntity
import pandas as pd
import os

class DataValidation:
    def __init__(self):
        pass
    
    def validate(self,config: DataValidationConfig):
        validation_status = True
        input_data = pd.read_csv(config.source_file)
        input_data_cols = list(input_data.columns)
        
        if len(input_data_cols) == len(list(config.schema.keys())): 
            validation_status = True
        else: 
            validation_status = False
            
        for col in input_data_cols:
            if col in list(config.schema.keys()):
                validation_status = True
            
            else:
                validation_status = False
                
        status_txt = os.path.join(config.root_dir,config.status_file_name)
        
        with open(status_txt,"w") as file:
            file.write(f"validation_status : {validation_status}")
            
        