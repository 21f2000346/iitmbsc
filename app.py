import streamlit as st
import pandas as pd
 
#Get Input
 
st.title('ODD OR EVEN')
st.header('Check the Number is Odd or Even')
x = st.number_input("Please Enter a Natural Number",min_value=0,step=1)
if(st.button("Check ODD or EVEN")):
    if (x%2 ==0) :
        st.subheader("You have Entered an EVEN number")
    else:
        st.subheader("You have Entered an ODD number")
