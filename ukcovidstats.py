import fypconnect
import getinput
import datetime
from datetime import datetime
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from PIL import Image
import streamlit as st

def highlight_errors(start, end):
    color = "red" if start > end else "white"
    return "background-color: %s" % color

def main():
    #title
    st.write("""
    # UK Covid Stats
    Graphs containing statistics from UK Covid pandemic
    """)
    left_column, right_column = st.beta_columns(2)
    #Image
    image = Image.open('C:/Users/aliab/PycharmProjects/Covid19/pictures/6000.jpg')
    st.image(image, caption='UK COVID19', use_column_width=True)

    #Get the data
    data = fypconnect.myresult_uk_death[::-1]
    column_names = fypconnect.field_names_uk_death
    #Set a subheader
    st.subheader('Uk deaths by date:')

    #Create a data frame
    df = pd.DataFrame(data, columns=column_names)

    #Show data as a table
    df = df.rename(columns={'ID': 'index'}).set_index('index')
    st.dataframe(df)

    #Show statistics
    st.write(df.describe())

    #Show data as a chart
    chart = st.bar_chart(data)

    #Split data into x and y
    x = df.iloc[:, -1].values
    y = df.iloc[:, 0:8].values
    #Split the data into train and test sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)

    #Store user input into variable
    temp_start = fypconnect.uk_death_date_start[4]
    temp_end = fypconnect.uk_death_date_end[4]
    user_input = getinput.get_user_input_uk_covid_deaths(temp_start, temp_end)

    #Set a subheader
    st.subheader('User input:')
    st.write(user_input)

    #Create and train the model
    #RandomForestClassifier = RandomForestClassifier(max_depth=2, random_state=0)
    #RandomForestClassifier.fit(x_train, y_train, sample_weight=None)

    #Show models metrics
    st.subheader('Model Test Accuracy Score:')
    #st.write(str(accuracy_score(y_test, RandomForestClassifier.predict(x_test)) *100) + '%')

    #Store the models predictions in variable
    #prediction = RandomForestClassifier.predict(user_input)

    #Set a subheader and display classificaiton
    st.subheader('Classification: ')
    #st.write(prediction)