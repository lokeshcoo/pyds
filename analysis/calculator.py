 #  streamlit is mainly used for creating frontend
import streamlit as st 

st.title("CALCULATOR")
st.markdown("Welcome to My First Streamlit App😎")

c1,c2=st.columns(2)   #for creating two columns
fnum=c1.number_input("enter the first number")
snum=c2.number_input("enetr the second number")

options = ["Add","Substract","Multiplication","Division"]
choice = st.radio("select an operation",options,horizontal=True)

button = st.button("Calculate")
if button:
    if choice == "Add":
        result=fnum+snum
    if choice == "Substract":
        result=fnum-snum
    if choice == "Multiplication":
        result=fnum*snum
    if choice == "Division":
        result=fnum/snum  
st.success(f"result is {result}")  






