import streamlit as st
import pickle
import numpy as np
import pandas as pd

pipe_preprocess = pickle.load(open("E:\Live project\production\streamlit\pipe_preprocess.pkl",'rb'))

st.set_page_config(page_title='Fraud Detection')

st.title('Online Betting Fraud Detection for Soccer')

#add a sidebar
st.sidebar.subheader("Import Files")
st.subheader('Demo File Format')
sample_df = pd.read_csv("E:\Live project\production\streamlit\Sample_Demo.csv")
st.write(sample_df)
test_case = st.sidebar.file_uploader(label = "Upload your csv file",
                         type = ['csv'])

global df
if test_case is not None:

    df = pd.read_csv(test_case)
try:
    st.subheader('File uploaded')
    st.write(df)
except Exception as e:
    print(e)
    st.write("Please upload file")


if st.button('Predict Fraud'):
   x = pd.Series(pipe_preprocess.predict(df))
   x.replace(to_replace = [0,1], value = ['ok', 'Fraud'], inplace=True)
   st.write(f'Prediction:',x)
   


   
   
   
   
   

   
