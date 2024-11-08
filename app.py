from src.iris.pipeline.training_pipeline import Training_Pipeline
from src.iris.pipeline.prediction_pipeline import Prediction_Pipeline
import streamlit as st
import numpy as np
from box import ConfigBox

st.title('Iris Classification')
st.write('Enter the values for prediction:')

feature1 = st.text_input("Sepal-Length")
feature2 = st.text_input("Sepal-Width")
feature3 = st.text_input("Petal-Length")
feature4 = st.text_input("Petal-Width")

pred = Prediction_Pipeline()


if st.button('Predict'):
    feature1 = float(feature1)
    feature2 = float(feature2)
    feature3 = float(feature3)
    feature4 = float(feature4)
    
    input_data = np.array([feature1, feature2, feature3, feature4])
    input_data = input_data.reshape(1,-1)
    prediction = pred.prediction(input_data)
    st.write(f"#### {prediction[0]}")
    