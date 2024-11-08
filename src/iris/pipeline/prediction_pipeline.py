import pickle
import numpy as np

class Prediction_Pipeline:
    
    def __init__(self):
        with open("artifacts/model_trainer/model.pkl","rb") as model_file:
            self.model = pickle.load(model_file)
            
        with open("artifacts/data_transformation/preprocessor.pkl","rb") as trf_file:
            self.data_transformer = pickle.load(trf_file)
            
    def prediction(self,arr:np.ndarray):
        model_predict = self.model.predict(arr)
        prediction = self.data_transformer.inverse_transform(model_predict)
        #prediction = self.data_transformer.inverse_transform(prediction)
        return prediction