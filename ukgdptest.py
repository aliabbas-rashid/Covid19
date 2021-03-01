import datetime
from datetime import datetime

import streamlit as st
import pandas as pd
from PIL import Image

import fypconnect
import getinput


def main():


    # title
    st.write("""
        # TEST
        """)

    # Image
    image = Image.open('C:/Users/aliab/PycharmProjects/Covid19/pictures/8000.jpg')
    st.image(image, caption='UK FLAG', use_column_width=True)

    # Data
    data = fypconnect.myresult_uk_gdp
    column_names = fypconnect.field_names_uk_gdp

    # Set a subheader
    st.subheader('UK GDP data:')

    # Create a data frame
    df = pd.DataFrame(data, columns=column_names)

    # Show data as a table
    df = df.rename(columns={'id': 'index'}).set_index('index')
    st.dataframe(df)

    # Show statistics
    st.subheader('Data Statistics:')
    st.write(df.describe())

    # Show data as a chart
    data_list_id = [x[0] for x in data]
    data_list_gdp = [x[2] for x in data]
    list_out = []
    for i in range(0, len(data_list_gdp)):
        list_out.append(data_list_id[i])
        list_out.append(data_list_gdp[i])

    list_df = zip(list_out[::2], list_out[1::2])
    list_comp = list(list_df)
    chart_data = pd.DataFrame(list_comp, columns=['id', 'gdp'])
    st.subheader('Data drawn as a line chart:')
    st.line_chart(chart_data)

    # Store user input into variable
    temp_start = fypconnect.uk_gdp_date_start[1]
    temp_end = fypconnect.uk_gdp_date_end[1]
    start_date_obj = datetime.strptime(temp_start, '%Y-%m-%d')
    end_date_obj = datetime.strptime(temp_end, '%Y-%m-%d')
    user_input = getinput.get_user_input_uk_gdp(start_date_obj, end_date_obj)

    # Set a subheader
    st.subheader('User input:')
    st.write(user_input[0])
    user_input_list = [item for item in data if ((datetime.strptime(item[1], '%Y-%m-%d') > user_input[1]) and (
                datetime.strptime(item[1], '%Y-%m-%d') < user_input[2]))]
    user_data_list_id = [x[0] for x in user_input_list]
    user_data_list_date = [x[1] for x in user_input_list]
    user_data_list_gdp = [x[2] for x in user_input_list]

    user_list_out = []
    for i in range(0, len(user_data_list_date)):
        user_list_out.append(user_data_list_gdp[i])
        user_list_out.append(user_data_list_date[i])

    user_list_df = zip(user_list_out[::2], user_list_out[1::2])
    user_list_comp = list(user_list_df)

    user_input_chart_data = pd.DataFrame(user_list_comp, columns=['gdp', 'date'])
    st.subheader('Data drawn as a line chart using user input:')
    #user_input_chart_data = user_input_chart_data.rename(columns={'gdp': 'index'}).set_index('index')
    st.line_chart(user_input_chart_data)
    st.write(user_list_comp)

    # Create and train the model
    x = user_data_list_id
    y = user_data_list_gdp
    # RandomForestClassifier.fit(x_train, y_train)

    # Show models metrics
    st.subheader('Model Test Accuracy Score:')
    # st.write(str(accuracy_score(y_test, RandomForestClassifier.predict(x_test)) *100) + '%')

    # Store the models predictions in variable
    # prediction = RandomForestClassifier.predict(user_input)

    # Set a subheader and display classificaiton
    st.subheader('Classification: ')
    # st.write(prediction)
