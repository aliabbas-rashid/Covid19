import fypconnect
import getinput
import datetime

import mltest
import mltest2
import mltest3
import ukgdpml
import newmltest
from datetime import datetime
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier
from PIL import Image
import streamlit as st


def main():
    # title
    st.write("""
    #  UK Gross Domestic Product
    Graph for the GDP for the UK
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
    data_list_date = [x[1] for x in data]
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

    # Get prediction date
    temp1 = "2021-03-01"
    temp2 = "2022-03-01"
    pred_start_date_obj = datetime.strptime(temp1, '%Y-%m-%d')
    pred_end_date_obj = datetime.strptime(temp2, '%Y-%m-%d')
    pred = getinput.get_predict_input(pred_start_date_obj, pred_end_date_obj)

    # Set a subheader
    st.subheader('User input:')
    st.write(user_input[0])
    user_input_list = [item for item in data if ((datetime.strptime(item[1], '%Y-%m-%d') > user_input[1]) and (datetime.strptime(item[1], '%Y-%m-%d') < user_input[2]))]
    user_data_list_id = [x[0] for x in user_input_list]
    user_data_list_date = [x[1] for x in user_input_list]
    user_data_list_gdp = [x[2] for x in user_input_list]

    user_list_out = []
    for i in range(0, len(user_data_list_gdp)):
        user_list_out.append(user_data_list_id[i])
        user_list_out.append(user_data_list_gdp[i])
    user_list_df = zip(user_list_out[::2], user_list_out[1::2])
    user_list_comp = list(user_list_df)

    user_input_chart_data = pd.DataFrame(user_list_comp, columns=['id', 'gdp'])
    st.subheader('Data drawn as a line chart using user input:')
    st.line_chart(user_input_chart_data)

    # Create and train the model
    modelX_list_out_a = []
    modelX_list_out_b = []
    modelX_list_out_c = []
    for i in range(0, len(data_list_id)):
        modelX_list_out_a.append(data_list_date[i])
        modelX_list_out_b.append(data_list_gdp[i])
        if i <= 126:
            modelX_list_out_c.append("Train")
        if i > 126:
            modelX_list_out_c.append("Test")
    modelX_list_out_df = zip(modelX_list_out_a, modelX_list_out_b, modelX_list_out_c)
    modelX_list_out_comp = list(modelX_list_out_df)
    df2 = pd.DataFrame(modelX_list_out_comp, columns=['Date', 'gdp', 'Class'])
    pred2 = []
    pred2.append(pred[1].strftime('%Y-%m-%d'))
    predict = pd.DataFrame(pred2, columns=['Date'])
    #ukgdpml.main(df2, predict)
    mltest.main(df2)
    """
    X = modelX_list_out_comp
    y = user_data_list_gdp
    model = DecisionTreeClassifier()
    st.write(X)
    st.write(type(y[0]))
    model.fit(X, y)
    predictions = model.predict([[datetime.date('2021-02-01')]])
    st.write(predictions)
    # RandomForestClassifier.fit(x_train, y_train)

    # Show models metrics
    st.subheader('Model Test Accuracy Score:')
    # st.write(str(accuracy_score(y_test, RandomForestClassifier.predict(x_test)) *100) + '%')

    # Store the models predictions in variable
    # prediction = RandomForestClassifier.predict(user_input)

    # Set a subheader and display classificaiton
    st.subheader('Classification: ')
    # st.write(prediction)
    """