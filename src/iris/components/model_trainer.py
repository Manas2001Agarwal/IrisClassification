import os
import sys
import pickle
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,classification_report
from src.iris.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    
    def __init__(self,config:ModelTrainerConfig):
        self.config = config
    
    def train_evaluate_model(self):
        train_data = pd.read_csv(self.config.source_train_file)
        rf = RandomForestClassifier(**self.config.params)
        rf.fit(train_data.iloc[:,:-1],train_data.iloc[:,-1])
        
        test_data = pd.read_csv(self.config.source_test_file)
        accuracy = accuracy_score(rf.predict(test_data.iloc[:,:-1]),test_data.iloc[:,-1])
        class_report = classification_report(rf.predict(test_data.iloc[:,:-1]),test_data.iloc[:,-1])
        
        with open(self.config.model_file_path,"wb") as file:
            pickle.dump(rf,file)
        
        return accuracy,class_report
        