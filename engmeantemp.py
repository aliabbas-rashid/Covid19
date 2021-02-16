import fypconnect
import getinput
import datetime
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from PIL import Image
import streamlit as st

def main():
    #title
    st.write("""
    # Pakistan Covid Profile
    Graphs containing statistics from Pakistan COVID Pandemic
    """)

    #Image
    image = Image.open('C:/Users/aliab/PycharmProjects/Covid19/2000.png')
    st.image(image, caption='TEMP', use_column_width=True)

    #Data
    data = fypconnect.myresult_eng_mean_temp

    #Set a subheader
    st.subheader('England Mean Temperature: ')

    #Show data as a table
    st.dataframe(data)

    #Show statistics
    #st.write(data.describe())

    #Show data as a chart
    chart = st.bar_chart(data)

    #Store user input into variable
    user_input = getinput.get_user_input_eng_mean_temp()

    #Set a subheader
    st.subheader('User input:')
    st.write(user_input)

    #Create and train the model
    #RandomForestClassifier = RandomForestClassifier()
    #RandomForestClassifier.fit(x_train, y_train)

    #Show models metrics
    st.subheader('Model Test Accuracy Score:')
    #st.write(str(accuracy_score(y_test, RandomForestClassifier.predict(x_test)) *100) + '%')

    #Store the models predictions in variable
    #prediction = RandomForestClassifier.predict(user_input)

    #Set a subheader and display classificaiton
    st.subheader('Classification: ')
    #st.write(prediction)