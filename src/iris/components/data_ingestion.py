import pandas as pd
from src.iris.entity.config_entity import DataIngestionConfig
class DataIngestion:
    def __init__(self):
        pass
    
    def download_data(self,config:DataIngestionConfig):
        data = pd.read_csv(config.source_file)
        data.to_csv(config.raw_data_file_path,index=False)