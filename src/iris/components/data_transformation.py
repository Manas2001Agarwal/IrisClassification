import sys
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from src.iris.entity.config_entity import DataTransformationConfig
import pickle

class DataTransformation:
    
    def __init__(self):
        pass
    
    def transform_data(self,config:DataTransformationConfig):
        data = pd.read_csv(config.source_file)
        
        label_encoder = LabelEncoder()
        label_encoder.fit(data['variety'])
        data['variety'] = label_encoder.transform(data['variety'])
        
        train,test = train_test_split(data,test_size=0.2,random_state=42)
        
        os.makedirs(os.path.dirname(config.train_file_name))
        
        train.to_csv(config.train_file_name,index=False)
        test.to_csv(config.test_file_name,index=False)
        
        with open(config.preprocessor_file_path,"wb") as file:
            pickle.dump(label_encoder,file=file)
        