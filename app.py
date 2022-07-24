import streamlit as st
import pandas as pd
 
#Get Input
 
st.title('ODD OR EVEN')
st.header('Check Number is Odd or Even')
x = st.number_input("GET_NUMBER",min_value=0,step=1)
if(st.button("Check ODD or EVEN")):
    if (x%2 ==0) :
        st.subheader("You have Entered an EVEN number")
    else:
        st.subheader("You have Entered an ODD number")
