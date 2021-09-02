# -*- coding: utf-8 -*-


from flask import Flask,request
import pandas as pd 
import numpy as np
import pickle
import streamlit as st

import PIL as Image


pickle_in = open('classifier.pkl', 'rb')
classifier =pickle.load(pickle_in)

def welcome(): 
    return "welcome ALL"

#validate the features inputs
def predict_note_authentication(variance, skewness, curtosis, entropy):
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    print(prediction)
    return prediction

def main():
    st.title("Bank Note Authenticator")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator Notes ML App </h2>
    </div>
    """
    
    st.markdown(html_temp, unsafe_allow_html=True)
    variance = st.text_input("Variance", "Type here")
    skewness = st.text_input("Skewness", "Type here")
    curtosis = st.text_input("Curtosis", "Type here")
    entropy  = st.text_input("Entropy", "Type here")

    result=""
    if st.button("Predict"):
        result = predict_note_authentication(
            variance,
            skewness, 
            curtosis,
            entropy)
    st.success('The output is {}'.format(result))

    if st.button("About"):
        st.text("Built With Streamlit ") 
if __name__ == '__main__':
    main()





