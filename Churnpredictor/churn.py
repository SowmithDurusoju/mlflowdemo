import streamlit as st
st.title("Bank churn predictor")
cibil=st.number_input("Enter your cibil score")
gender=st.selectbox('select your Gender',['Male','Female'])
st.number_input("Enter your age")
st.number_input("Enter your tenure")
st.number_input("Enter your account balance")
