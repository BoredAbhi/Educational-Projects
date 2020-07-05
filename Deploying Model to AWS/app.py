# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 10:17:27 2020

@author: Abhijeet
"""

# Serve model as a flask application

import pickle
import numpy as np
from flask import Flask, request

model = None

# Innstanciate Flask object
app = Flask(__name__)

# Loading our saved model from pickle file
def load_model():
    global model
    # model variable refers to the global variable
    with open('iris_trained_model.pkl', 'rb') as f:
        model = pickle.load(f)


@app.route('/')
def home_endpoint():
    return 'Hello World!'

# Note : In Windows curl uses double quotes only !

@app.route('/predict', methods=['POST'])
def get_prediction():
    # Works only for a single sample
    if request.method == 'POST':
        data = request.get_json()  # Get data posted as a json
        data = np.array(data)[np.newaxis, :]  # converts shape from (4,) to (1, 4)
        prediction = model.predict(data)  # runs globally loaded model on the data
    return str(prediction[0])


if __name__ == '__main__':
    load_model()  # load model at the beginning once only
    app.run(host='127.0.0.1', port=8000)
  