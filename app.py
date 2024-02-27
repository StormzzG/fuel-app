import streamlit as st
import joblib 

st.set_page_config(page_icon=':car:',page_title='CO2 Emissions')

st.title(':car: Car CO2 Emissions Predictor')

st.image('05(1).jpg')

st.markdown('This web app is built on a Supervised Multiple Linear Regression Machine Learning Algorithm for predicting the CO2 emissions of cars based on engine size, number of cylinders and fuel consumption. Fill in the fields below to have a look!')
st.markdown('-----------------------------------')

with open('Fuel-Predictor.joblib','rb') as f:
    model = joblib.load(f)

col1,col2 = st.columns((2))
with col1:
    engine = float(st.number_input('Engine Size'))
with col2:
    cylinders = int(st.number_input('Number of Cylinders'))
fuel = float(st.number_input('Fuel Consumption(L/100Km)'))

submit_button = st.button('Predict')
if submit_button:
    if engine and not cylinders and not fuel:
        st.error('Please fill all requirements')
    if engine and not cylinders and fuel:
        st.error('Please fill all requirements')
    if engine and cylinders and not fuel:
        st.error('Please fill all requirements')
    if not engine and not cylinders and not fuel:
        st.error('Please fill all requirements')
    if not engine and not cylinders and fuel:
        st.error('Please fill all requirements')
    if not engine and cylinders and not fuel:
        st.error('Please fill all requirements')
    if not engine and cylinders and fuel:
        st.error('Please fill all requirements')
    if engine and cylinders and fuel:
        prediction = model.predict([[engine,cylinders,fuel]])
        st.write(f"{int(prediction)} g/km")

    if prediction > 0 and prediction <= 150:
        st.write('Low Fuel Economy')
    elif prediction > 150 and prediction <= 255:
        st.write('Average Fuel Economy')
    elif prediction > 255:
        st.write('High Fuel Economy')