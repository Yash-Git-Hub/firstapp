import streamlit as st
st.title("Lets find out how healthy you are : ")

height = float( st.text_input("Enter Height in Centimeter ",0))
weight = float(st.text_input("Enter Weight   in Kg  ",0))
height=height/100

# ** is the power of operator i.e height*height in this case
if(weight>0):
    bmi = weight/(height**2) 
    st.write("## Your BMI is: {0:.2f} and you are: ".format(bmi), end='')
    if ( bmi < 16):
        st.write("## severely underweight")
        st.write("### You Need to Gain %s Kg weight to have a healthy bmi"%str(((25*height)/2)-weight))

    elif ( bmi >= 16 and bmi < 18.5):
        st.write("## underweight")
        st.write("### You Need to Gain %s Kg weight to have a healthy bmi"%str(((25*height)/2)-weight))

    elif ( bmi >= 18.5 and bmi < 25):
        st.write("## Healthy")

    elif ( bmi >= 25 and bmi < 30):
        st.write("## overweight")
        st.write("### You Need to reduce %s Kg weight to have a healthy bmi"%str((-(25*height)/2)+weight))

    elif ( bmi >=30):
        st.write("## severely overweight")
        st.write("### You Need to reduce %s Kg weight to have a healthy bmi"%str((-(25*height)/2)+weight))
    
