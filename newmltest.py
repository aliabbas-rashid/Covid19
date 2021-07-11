import numpy as np
import pandas as pd
from datetime import datetime
import fypconnect
import sklearn.linear_model
from sklearn import linear_model
import streamlit as st
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.ar_model import AutoReg

def main(df):

    data_new = fypconnect.myresult_uk_gdp
    #st.write(data_new)

    gdp_column = fypconnect.myresult_gdp_column
    date_column = fypconnect.myresult_date_column

    arrayofdates = []

    for dict in date_column:
        arrayofdates.append(dict(zip(date_column, dict)))

    st.write("DATE COLUMN")
    st.write(date_column)
    st.write("ARRAY OF DATES")
    st.write(arrayofdates)

    dataframe_new = pd.DataFrame({'date':date_column, 'gdp':gdp_column})
    st.write(dataframe_new)

    ml = sklearn.linear_model.LinearRegression()
    ml.fit(date_column, gdp_column)