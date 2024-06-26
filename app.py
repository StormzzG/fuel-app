import streamlit as st
import joblib 
import pandas as pd

st.set_page_config(page_icon=':car:',page_title='CO2 Emissions Prediction')

st.title(':car: Car CO2 Emissions Predictor')

st.image('porsche.jpg')

st.markdown('This web app is built on a Supervised Random Forest Regression, Machine Learning Algorithm for predicting the CO2 emissions of cars based on engine size, number of cylinders and fuel consumption. Fill in the fields below to have a look! [Here](https://github.com/StormzzG/machine-learning) is a link to a python notebook that shows how the model was trained.')
st.markdown('-----------------------------------')

with open('fuel-predictor2.joblib','rb') as f:
    model = joblib.load(f)

col1,col2 = st.columns((2))
with col1:
    engine = float(st.number_input('Engine Size'))
with col2:
    cylinders = int(st.number_input('Number of Cylinders'))
fuel = float(st.number_input('Fuel Consumption Combined(L/100Km)'))

submit_button = st.button('Predict')
if submit_button:
    if engine and not cylinders and not fuel:
        st.error('Please fill all requirements')
        prediction = 0
    if engine and not cylinders and fuel:
        st.error('Please fill all requirements')
        prediction = 0
    if engine and cylinders and not fuel:
        st.error('Please fill all requirements')
        prediction = 0
    if not engine and not cylinders and not fuel:
        st.error('Please fill all requirements')
        prediction = 0
    if not engine and not cylinders and fuel:
        st.error('Please fill all requirements')
        prediction = 0
    if not engine and cylinders and not fuel:
        st.error('Please fill all requirements')
        prediction = 0
    if not engine and cylinders and fuel:
        st.error('Please fill all requirements')
        prediction = 0
    if engine and cylinders and fuel:
        prediction = model.predict([[engine,cylinders,fuel]])
        st.write(f"{int(prediction)} g/km")

    if prediction > 0 and prediction <= 150:
        st.write('Low Fuel Economy')
    elif prediction > 150 and prediction <= 255:
        st.write('Average Fuel Economy')
    elif prediction > 255:
        st.write('High Fuel Economy')

st.subheader('Sample Data used for Training and Testing')
df = pd.read_csv('Fuel_data.csv')
st.dataframe(df.head().style.background_gradient(cmap='Oranges'))