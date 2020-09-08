import streamlit as st


height = float( st.text_input("Enter height in cm ", 1))
weight = float(st.text_input("Enter hwight  in kg ", 1))

# the formula for calculating bmi

bmi = weight/(height**2) 
# ** is the power of operator i.e height*height in this case

st.write("Your BMI is: {0} and you are: ".format(bmi), end='')

#conditions
if ( bmi < 16):
   st.write("severely underweight")

elif ( bmi >= 16 and bmi < 18.5):
   st.write("underweight")

elif ( bmi >= 18.5 and bmi < 25):
   st.write("Healthy")

elif ( bmi >= 25 and bmi < 30):
   st.write("overweight")

elif ( bmi >=30):
   st.write("severely overweight")