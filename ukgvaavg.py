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
    # title
    st.write("""
    #  UK Gross Value Added (average)
    Graphs containing statistics of the UK's GVA (average)
    """)

    # Image
    image = Image.open('C:/Users/aliab/PycharmProjects/Covid19/pictures/1000.jpg')
    st.image(image, caption='GVA', use_column_width=True)

    # Data
    data = fypconnect.myresult_uk_gva
    column_names = fypconnect.field_names_uk_gva

    # Set a subheader
    st.subheader('England Gross Value Added: ')

    # Create data frame
    df = pd.DataFrame(data, columns=column_names)

    # Show data as a table
    st.dataframe(df)

    # Show statistics
    st.write(df.describe())

    # Show data as a chart
    chart = st.line_chart(data)

    # Store user input into variable
    user_input = getinput.get_user_input_uk_gva()

    # Set a subheader
    st.subheader('User input:')
    st.write(user_input)

    # Create and train the model
    # RandomForestClassifier = RandomForestClassifier()
    # RandomForestClassifier.fit(x_train, y_train)

    # Show models metrics
    st.subheader('Model Test Accuracy Score:')
    # st.write(str(accuracy_score(y_test, RandomForestClassifier.predict(x_test)) *100) + '%')

    # Store the models predictions in variable
    # prediction = RandomForestClassifier.predict(user_input)

    # Set a subheader and display classificaiton
    st.subheader('Classification: ')
    # st.write(prediction)