import streamlit as st
import pickle
import numpy as np
import pandas as pd

pickle_in = open("C:/Users/Kazembe/model.json","rb")
model = pickle.load(pickle_in)


def predictChurn(PaperlessBilling,MonthlyCharges,SeniorCitizen,PaymentMethod,MultipleLines,TotalCharges,PhoneService):
    newChurn=pd.DataFrame([[PaperlessBilling,MonthlyCharges,SeniorCitizen,PaymentMethod,MultipleLines,TotalCharges,PhoneService]])
    prediction=model.predict(newChurn)
    print(prediction)
    return prediction



st.title("Churn Predictions")
html_temp = """
<div style = "background-color:tomato;padding:10px">
<h2 style = "color:white;text-align:center;">MELOEYAL TELECOMMUNICATIONS CHURN PREDICTOR</h2>
</div>
"""
st.markdown(html_temp,unsafe_allow_html=True)
PaperlessBilling = st.text_input("PaperlessBilling","Type Here")
MonthlyCharges = st.text_input("MonthlyCharges","Type Here")
SeniorCitizen = st.text_input("SeniorCitizen","Type Here")
PaymentMethod = st.text_input("PaymentMethod","Type Here")
MultipleLines = st.text_input("MultipleLines","Type Here")
TotalCharges = st.text_input("TotalCharges","Type Here")
PhoneService = st.text_input("PhoneService","Type Here")
result = ""

if st.button("Predict"):
    result = predictChurn(PaperlessBilling,MonthlyCharges,SeniorCitizen,PaymentMethod,MultipleLines,TotalCharges,PhoneService)
st.success(result)
    

