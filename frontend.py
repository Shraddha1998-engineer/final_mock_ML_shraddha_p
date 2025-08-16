import streamlit as st 
import pandas as pd 
import pickle 
st.set_page_config(page_title='Car_Price_Prediction')
st.header('Welcome to chennai car price predictor!!!!')
st.header('Please enter your details to continue...')
df=pd.read_csv('copied.csv')
with open('RFmodel.pkl','rb') as file:
    model=pickle.load(file)
with st.container(border=True):
    col1,col2=st.columns(2)
    make=col1.selectbox('Make',options=df['Make'].unique())
    model_=col2.selectbox('Model',options=df['Model'].unique())
    year=col1.selectbox('Year',options=df['Year'].unique())
    fuels=col2.selectbox('Fuel Type',options=df['Fuel Type'].unique())
    mileage=col1.number_input('Mileage',min_value=5,step=10)
    transmission=col1.selectbox('Transmission',options=df['Transmission'].unique())
    price=col2.number_input('Price',min_value=10000,step=1000)
    input_values=[(fuels.index(fuels),make.index(make),model_.index(model_),transmission.index(transmission),year,mileage,price)]
    c1,c2,c3=st.columns([1.6,1.5,1])
    if c2.button('Predict_price'):
       out=model.predict(input_values)
       st.subheader(f'total_price💰: {out[0]}')
    
    


