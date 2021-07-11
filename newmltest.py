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

    #df_new = pd.read_excel(r'C:\Users\aliab\PycharmProjects\Covid19\data.xlsx')
    #st.write(df_new)

    data_new = fypconnect.myresult_uk_gdp
    #st.write(data_new)

    gdp_column = fypconnect.myresult_gdp_column
    date_column = fypconnect.myresult_date_column
    date_list = list(date_column)
    st.write("THIS IS DATE LIST")
    st.write(type(date_column[1]))

    list_out = []
    for i in gdp_column:
        list_out.append(list(i))

    st.write("!£Q$£$%£%^£^£$!£")
    st.write(list_out)

    list_out_2 = []
    for i in date_column:
        list_out_2.append(pd.to_datetime(list(i)))

    st.write("LIST INIT")
    st.write(list_out_2)

    dataframe_new = pd.DataFrame({'date':list_out_2, 'gdp':list_out})
    st.write("THIS IS NEW DATA FRAME")
    st.write(dataframe_new)

    ml = sklearn.linear_model.LinearRegression()
    ml.fit(list_out_2, list_out)

    