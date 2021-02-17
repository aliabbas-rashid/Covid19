import streamlit as st
import datetime
import pandas as pd

#Get feature input from user for pakistan covid profile
def get_user_input_pakistan():
    date_input_start = st.sidebar.slider('Pakistan- Start Date:', datetime.date(2020, 1, 1), datetime.date(2021, 1, 24), datetime.date(2020, 4, 8))
    date_input_end = st.sidebar.slider('Pakistan- End Date:', datetime.date(2020, 1, 1), datetime.date(2021, 1, 24), datetime.date(2020, 4, 8))

    #Store a dictionary into a variable
    user_data = {'Pakistan- Start Date:':date_input_start,
                 'Pakistan- End Date:':date_input_end}
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
    date_input_start = st.sidebar.slider('UK Deaths- Start Date:', datetime.date(2020, 1, 1), datetime.date(2021, 1, 24), datetime.date(2020, 4, 8))
    date_input_end = st.sidebar.slider('UK Deaths- End Date:', datetime.date(2020, 1, 1), datetime.date(2021, 1, 24), datetime.date(2020, 4, 8))

    #Store a dictionary into a variable
    user_data = {'UK Deaths- Start Date:':date_input_start,
                 'UK Deaths- End Date:':date_input_end}
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
    date_input_start = st.sidebar.slider('UK GDP- Start Date:', datetime.date(2020, 1, 1), datetime.date(2021, 1, 24), datetime.date(2020, 4, 8))
    date_input_end = st.sidebar.slider('UK GDP- End Date:', datetime.date(2020, 1, 1), datetime.date(2021, 1, 24), datetime.date(2020, 4, 8))

    #Store a dictionary into a variable
    user_data = {'UK GDP- Start Date:':date_input_start,
                 'UK GDP- End Date:':date_input_end}
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
def get_user_input_eng_mean_temp():
    date_input_start = st.sidebar.slider('UK Mean Temp- Start Date:', datetime.date(2020, 1, 1), datetime.date(2021, 1, 24), datetime.date(2020, 4, 8))
    date_input_end = st.sidebar.slider('UK Mean Temp- End Date:', datetime.date(2020, 1, 1), datetime.date(2021, 1, 24), datetime.date(2020, 4, 8))

    #Store a dictionary into a variable
    user_data = {'UK Mean Temp- Start Date:':date_input_start,
                 'UK Mean Temp- End Date:':date_input_end}
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
def get_user_input_uk_gva():
    date_input_start = st.sidebar.slider('UK GVA- Start Date:', datetime.date(2020, 1, 1), datetime.date(2021, 1, 24), datetime.date(2020, 4, 8))
    date_input_end = st.sidebar.slider('UK GVA- End Date:', datetime.date(2020, 1, 1), datetime.date(2021, 1, 24), datetime.date(2020, 4, 8))

    #Store a dictionary into a variable
    user_data = {'UK GVA- Start Date:':date_input_start,
                 'UK GVA- End Date:':date_input_end}
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

#MERGE TUPLES
def merge_tuples(*t): return tuple(j for i in (t) for j in (i if isinstance(i, tuple) else (i,)))