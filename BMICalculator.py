import streamlit as st
st.title("Calculate your BMI, Stay Fit and Healthy!")
weight = st.number_input("Enter your weight in kg:")
status = st.radio('Select your height in',('cms','meters','feet'))
if status=='cms':
   height=st.number_input("Centimeters")
   try:
      bmi=weight/((height/100)**2)
   except:
      st.text("Enter the correct value")
elif status=='meters':
   height=st.number_input("Meters")
   try:
     bmi=weight/(height*height)
   except:
      st.text("Enter the correct value") 
elif status =='feet':
   height=st.number_input("Feet:")
   try:
     bmi=weight/((height/3.28)**2)
   except:
       st.text("Enter the correct value")

if(st.button("Calculate BMI")):
   st.text(f"Your bmi is {bmi}")
   if bmi>=16 and bmi<18:
      st.warning("You are under weight")
   elif bmi>=18 and bmi<25:
      st.success("You are healthy")
   elif bmi>=25 and bmi<30:
      st.warning("You are overweight")
   else:
      st.error("Yor are under obese category")