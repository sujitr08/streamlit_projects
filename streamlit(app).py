import streamlit as st
import time as t

# to insert and image
st.image("learn obj.png")

# title-- used to add the title of an app
st.title("Welcome to Intellipaat")

# Header
st.header("Machine Learning")

# Sub Header
st.subheader("Linear Regression")

# Information
st.info("Information details of a user")

# Warning msg
st.warning("Come on time or else you will be marked absent")

#write func
st.write("Employee name")
st.write("range(50)")
st.write(range(50))

# Wrong or error msg
st.error("Wrong password")

# Success msg
st.success("Congrats! you got A grade")

# Markdown func
st.markdown("# Intellipaat")
st.markdown("## Intellipaat")
st.markdown("### Intellipaat")
st.markdown(":moon:")

# text
st.text("Intellipaat learners have to achieve 80% marks in every subject")

# to give a caption
st.caption("Caption here")

# to display a mathematical equation
st.latex(r''' a+b x^2+c ''')

#Widgets

st.checkbox('Login')
st.button('Click')
st.radio("Pick your Gender", ["Male", "Female", "Other"])
st.selectbox("Pick your Course", ["ML", "Cloud", "Cyber Security"])
st.multiselect("Choose the Department", ["Sales & Marketing", "Prod & QA", "DevOps"])
st.select_slider("Ratings",["Bad", "Good", "Excellent", "Outsanding"])
st.slider("Enter your number",0,30)
st.number_input("Pick a number",0,10)
st.text_input("Enter Your email Id")
st.date_input("Opening Cermony")
st.time_input("Display Time")
st.text_area("Welcome to Intellipaat, Leave your comments")

# for uploading a file
st.file_uploader("Upload your file")

#color picker
st.color_picker("Color")

#to show progress
st.progress(90)

#spinner func
#with st.spinner("Just Wait"):
    #t.sleep(2)

#ballon on screen page
st.balloons()

#sidebar layouts
st.sidebar.title("Intellipaat")
st.sidebar.text_input("Login Id")
st.sidebar.text_input("Password")
st.sidebar.button("Submit")
st.sidebar.radio("Professional Expertise",["Student", "Professional", "Others"])

# Data Visualisation
import pandas as pd
import numpy as np
st.title("Bar Chart")
data=pd.DataFrame(np.random.randn(50,2),columns=["x","y"])
st.bar_chart(data)
st.title("Line Chart")
st.line_chart(data)
st.title("Area Chart")
st.area_chart(data)





