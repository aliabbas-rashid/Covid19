import streamlit as st
import datetime
import pandas as pd

#Get feature input from user for pakistan covid profile
def get_user_input_pakistan():
    date_input_start = st.sidebar.slider('Start Date Pakistan', datetime.date(2020, 1, 1), datetime.date(2021, 1, 24), datetime.date(2020, 4, 8))
    date_input_end = st.sidebar.slider('End Date Pakistan', datetime.date(2020, 1, 1), datetime.date(2021, 1, 24), datetime.date(2020, 4, 8))

    #Store a dictionary into a variable
    user_data = {'Start Date Pakistan':date_input_start,
                 'End Date Pakistan':date_input_end}
    #color = "red" if date_input_start > date_input_end or date_input_start == date_input_end else "white"
    if date_input_start > date_input_end:
        st.markdown("**ERROR**: Start date cannot be after the End date")
        st.write(ValueError)
    elif date_input_start == date_input_end:
        st.markdown("**ERROR**: Start date cannot be the same as the End date")
        st.write(ValueError)
    #Transform the data into data frame
    features = pd.DataFrame(user_data, index=[0])
    #st.dataframe(features.applymap(f'color: {color}'))
    return features


#Get feature input from user for uk covid deaths
def get_user_input_uk_covid_deaths():
    date_input_start = st.sidebar.slider('Start Date UK Deaths', datetime.date(2020, 1, 1), datetime.date(2021, 1, 24), datetime.date(2020, 4, 8))
    date_input_end = st.sidebar.slider('End Date UK Deaths', datetime.date(2020, 1, 1), datetime.date(2021, 1, 24), datetime.date(2020, 4, 8))

    #Store a dictionary into a variable
    user_data = {'Start Date UK Deaths':date_input_start,
                 'End Date UK Deaths':date_input_end}
    #color = "red" if date_input_start > date_input_end or date_input_start == date_input_end else "white"
    if date_input_start > date_input_end:
        st.markdown("**ERROR**: Start date cannot be after the End date")
        st.write(ValueError)
    elif date_input_start == date_input_end:
        st.markdown("**ERROR**: Start date cannot be the same as the End date")
        st.write(ValueError)
    #Transform the data into data frame
    features = pd.DataFrame(user_data, index=[0])
    #st.dataframe(features.applymap(f'color: {color}'))
    return features

#Get feature input from user
def get_user_input_uk_gdp():
    date_input_start = st.sidebar.slider('Start Date UK GDP', datetime.date(2020, 1, 1), datetime.date(2021, 1, 24), datetime.date(2020, 4, 8))
    date_input_end = st.sidebar.slider('End Date UK GDP', datetime.date(2020, 1, 1), datetime.date(2021, 1, 24), datetime.date(2020, 4, 8))

    #Store a dictionary into a variable
    user_data = {'Start Date UK GDP':date_input_start,
                 'End Date UK GDP':date_input_end}
    #color = "red" if date_input_start > date_input_end or date_input_start == date_input_end else "white"
    if date_input_start > date_input_end:
        st.markdown("**ERROR**: Start date cannot be after the End date")
        st.write(ValueError)
    elif date_input_start == date_input_end:
        st.markdown("**ERROR**: Start date cannot be the same as the End date")
        st.write(ValueError)
    #Transform the data into data frame
    features = pd.DataFrame(user_data, index=[0])
    #st.dataframe(features.applymap(f'color: {color}'))
    return features