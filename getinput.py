import streamlit as st
import datetime
import time
import pandas as pd

# Get feature input from user for pakistan covid profile
def get_user_input_pakistan(start, end):
    midpoint = start + (end - start) / 2
    date_input_start = st.sidebar.slider('Pakistan- Start Date:', start, end, midpoint)
    date_input_end = st.sidebar.slider('Pakistan- End Date:', start, end, midpoint)

    # Store a dictionary into a variable
    user_data = {'Pakistan- Start Date:':date_input_start,
                 'Pakistan- End Date:':date_input_end}
    # color = "red" if date_input_start > date_input_end or date_input_start == date_input_end else "white"
    if date_input_start > date_input_end:
        st.markdown("**ERROR**: Start date cannot be after the End date")
        st.write(ValueError)
    elif date_input_start == date_input_end:
        st.markdown("**ERROR**: Start date cannot be the same as the End date")
        st.write(ValueError)
    # Transform the data into data frame
    features = pd.DataFrame(user_data, index=[0])
    return features


# Get feature input from user for uk covid deaths
def get_user_input_uk_covid_deaths(start, end):
    midpoint = start + (end - start) / 2
    st.write(end)
    date_input_start = st.sidebar.slider('UK Deaths- Start Date:', start, end, midpoint)
    date_input_end = st.sidebar.slider('UK Deaths- End Date:', start, end, midpoint)

    # Store a dictionary into a variable
    user_data = {'UK Deaths- Start Date:':date_input_start,
                 'UK Deaths- End Date:':date_input_end}
    # color = "red" if date_input_start > date_input_end or date_input_start == date_input_end else "white"
    if date_input_start > date_input_end:
        st.markdown("**ERROR**: Start date cannot be after the End date")
        st.write(ValueError)
    elif date_input_start == date_input_end:
        st.markdown("**ERROR**: Start date cannot be the same as the End date")
        st.write(ValueError)
    features = pd.DataFrame(user_data, index=[0])
    return features

# Get feature input from user
def get_user_input_uk_gdp(start, end):
    midpoint = start + (end - start) / 2
    date_input_start = st.sidebar.slider('UK GDP- Start Date:', start, end, midpoint)
    date_input_end = st.sidebar.slider('UK GDP- End Date:', start, end, midpoint)
    wave1 = st.sidebar.button('Covid19 1st Wave [NOT WORKNG]')
    wave2 = st.sidebar.button('Covid19 2nd Wave [NOT WORKING]')
    if wave1:
        date_input_start = datetime.date(2020, 1, 1)
        date_input_end = datetime.date(2020, 8, 1)
        user_data = {'UK GDP- Start Date:': datetime.date(2020, 1, 1),
                     'UK GDP- End Date:': datetime.date(2020, 8, 1)}
        features = pd.DataFrame(user_data, index=[0])
        return features, date_input_start, date_input_end
    if wave2:
        date_input_start = datetime.date(2020, 8, 1)
        date_input_end = datetime.date(2020, 11, 1)
        user_data = {'UK GDP- Start Date:': datetime.date(2020, 8, 1),
                     'UK GDP- End Date:': datetime.date(2020, 11, 1)}
        features = pd.DataFrame(user_data, index=[0])
        return features, date_input_start, date_input_end

    # Store a dictionary into a variable
    user_data = {'UK GDP- Start Date:':date_input_start,
                 'UK GDP- End Date:':date_input_end}
    # color = "red" if date_input_start > date_input_end or date_input_start == date_input_end else "white"
    if date_input_start > date_input_end:
        st.markdown("**ERROR**: Start date cannot be after the End date")
        st.write(ValueError)
    elif date_input_start == date_input_end:
        st.markdown("**ERROR**: Start date cannot be the same as the End date")
        st.write(ValueError)
    # Transform the data into data frame
    features = pd.DataFrame(user_data, index=[0])
    return features, date_input_start, date_input_end

# Get feature for prediction from user
def get_predict_input(start, end):
    midpoint = start + (end - start) / 2
    predict_input = st.sidebar.slider('Prediction GDP date: ', start, end, midpoint)
    user_data = {'Predict date: ': predict_input}
    features = pd.DataFrame(user_data, index=[0])
    return features, predict_input

# Get feature input from user
def get_user_input_eng_mean_temp():
    a = datetime.date(2020, 1, 1)
    b = datetime.date(1999, 1, 1)
    midpoint = a + (b - a) / 2
    date_input_start = st.sidebar.slider('UK Mean Temp- Start Date:', datetime.date(1999, 1, 1), datetime.date(2020, 1, 1), midpoint)
    date_input_end = st.sidebar.slider('UK Mean Temp- End Date:', datetime.date(1999, 1, 1), datetime.date(2020, 1, 1), midpoint)

    # Store a dictionary into a variable
    user_data = {'UK Mean Temp- Start Date:':date_input_start,
                 'UK Mean Temp- End Date:':date_input_end}
    # color = "red" if date_input_start > date_input_end or date_input_start == date_input_end else "white"
    if date_input_start > date_input_end:
        st.markdown("**ERROR**: Start date cannot be after the End date")
        st.write(ValueError)
    elif date_input_start == date_input_end:
        st.markdown("**ERROR**: Start date cannot be the same as the End date")
        st.write(ValueError)
    # Transform the data into data frame
    features = pd.DataFrame(user_data, index=[0])
    return features

# Get feature input from user
def get_user_input_uk_gva():
    a = datetime.date(2020, 1, 1)
    b = datetime.date(1999, 1, 1)
    midpoint = a + (b - a) / 2
    date_input_start = st.sidebar.slider('UK GVA- Start Date:', datetime.date(1999, 1, 1), datetime.date(2020, 1, 1), midpoint)
    date_input_end = st.sidebar.slider('UK GVA- End Date:', datetime.date(1999, 1, 1), datetime.date(2020, 1, 1), midpoint)

    # Store a dictionary into a variable
    user_data = {'UK GVA- Start Date:':date_input_start,
                 'UK GVA- End Date:':date_input_end}
    # color = "red" if date_input_start > date_input_end or date_input_start == date_input_end else "white"
    if date_input_start > date_input_end:
        st.markdown("**ERROR**: Start date cannot be after the End date")
        st.write(ValueError)
    elif date_input_start == date_input_end:
        st.markdown("**ERROR**: Start date cannot be the same as the End date")
        st.write(ValueError)
    # Transform the data into data frame
    features = pd.DataFrame(user_data, index=[0])
    return features

def datetime_to_float(d):
    dt = datetime.datetime.strptime(d, '%Y-%m-%d')
    return dt.timestamp()

def float_to_datetime(fl):
    return datetime.datetime.fromtimestamp(fl)

def get_heathrow_input():
    st.sidebar.write("Inputs for machine learning:")
    st.sidebar.write("___")
    st.sidebar.write("Formatting:")
    st.sidebar.write("Year = YYYY")
    st.sidebar.write("Month = M (1-12)")
    st.sidebar.write("Temperature Min = INT")
    st.sidebar.write("Air Frost Days = INT")
    st.sidebar.write("Rain (mm) = INT")
    st.sidebar.write("Sunshine (hours) = INT")
    st.sidebar.write("___")
    year = st.sidebar.slider("Year", 1948, 2030, 1989)
    month = st.sidebar.slider("Month", 1, 12, 6)
    tmin = st.sidebar.slider("Temperature (minimum, rounded):", -5, 20, 8)
    af = st.sidebar.slider("Air Frost Days", 0, 31, 16)
    rain = st.sidebar.slider("Rainfall (mm, rounded):", 0, 200, 100)
    sun = st.sidebar.slider("Sunshine (hours, rounded)", 0, 350, 175)
    user_data = {'yyyy' : year,
                 'mm' : month,
                 'tmin' : tmin,
                 'af' : af,
                 'rain' : rain,
                 'sun' : sun}

    features = pd.DataFrame(user_data, index=[0])

    features.loc[features['rain']>=40, 'Recip Type'] = 1
    features.loc[features['rain'] < 40, 'Recip Type'] = 0

    features.loc[features['sun'] >= 60, 'Sun Type'] = 1
    features.loc[features['sun'] < 60, 'Sun Type'] = 0

    return features