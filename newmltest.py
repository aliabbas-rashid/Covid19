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

    st.write(fypconnect.myresult_gdp_column)
    st.write(fypconnect.myresult_date_column)