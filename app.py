import streamlit as st
import numpy as np
import joblib
# load the model
model=joblib.load('data.pkl')
# title of the application
st.title('TIP PREDICTOR APP')
# inputs of the application
total_bill=st.number_input("please enter the bill amount (in $s)",min_value=0.00,step=0.1)
sex=st.selectbox('sex',['Male','Female'])
smoker=st.selectbox('smoker',['Yes','No'])
day=st.selectbox('day',['Thur','Fri','Sat','Sun'])
time=st.selectbox('time',['Lunch','Dinner'])
size=st.number_input("please enter size of the group ",min_value=1,step=1)
# covert categorical inputs to numerical values
sex_value = 0 if sex == 'Male' else 1
smoker_value = 0 if smoker == 'No' else 1
time_value = 0 if time == 'Lunch' else 1
day_value = {"Thur":0, "Fri":1,"Sat":2,"Sun":3}[day]
# predict button
if st.button('predict'):
    # create a numpy array for the model input
    features = ([[total_bill,sex_value,smoker_value,time_value,day_value,size]])
    # predict the tip using the model
    result=model.predict(features)
    # display the prediction
    st.write(f"the predicted tip amount is ${result[0]:.2f}")