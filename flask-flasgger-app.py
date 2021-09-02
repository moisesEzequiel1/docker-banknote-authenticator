# -*- coding: utf-8 -*-


from flask import Flask,request
import pandas as pd 
import numpy as np
import pickle
import flasgger
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

pickle_in = open('classifier.pkl', 'rb')
classifier =pickle.load(pickle_in)

@app.route('/')
def welcome(): 
    return "welcome ALL"

#validate the features inputs
@app.route('/predict')
def predict_note_authentication():
    """Let's Authenticate the Banks Notes
    This and enpoint to bank-notes, to query type inputs
    ---
    parameters: 
      - name: variance
        in: query 
        type: number 
        require: true
      - name: skewness 
        in: query 
        type: number 
        require: true
      - name: curtosis
        in: query 
        type: number 
        require: true
      - name: entropy
        in: query 
        type: number 
        require: true
    responses: 
        200: 
            description: The output values
    """


    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')

    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    return "The prediction value is" + str(prediction)


@app.route('/predict_file',methods=["POST"])
def predict_note_file():
    """Let's  Authenticate the Banks Notes
    This is endpoint of the api-bank-note-validation, to file type input
    ---
    parameters: 
      - name: file
        in: formData 
        type: file 
        require: true
    responses: 
        200: 
            description: The output values
    """
    
    df_test = pd.read_csv(request.files.get("file"))
    X = df_test.iloc[:, :-1]
    prediction = classifier.predict(X)
    return "The prediction values for the csv is" + str(list((prediction)))





if __name__ == '__main__':
    app.run(host="0.0.0.0", port = 5000)






