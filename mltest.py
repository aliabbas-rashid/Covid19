import numpy as np
import pandas as pd
from datetime import datetime
from sklearn import linear_model
import streamlit as st
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
from statsmodels.tsa.stattools import adfuller

def main(df):
    df = df.drop(['Class'], axis=1)
    df['Date'] = pd.to_datetime(df['Date'], infer_datetime_format=True)
    indexedDataset = df.set_index(['Date'])

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot(df['Date'], df['gdp'])

    ax.set_xlabel("Date")
    ax.set_ylabel("GDP")
    st.write(fig)

    rolmean = indexedDataset.rolling(window=12).mean() # window is 12 for monthly basis
    rolstd = indexedDataset.rolling(window=12).std()

    fig2 = plt.figure()
    ax2 = fig2.add_subplot(1, 1, 1)
    ax2.plot(indexedDataset, color='blue', label='Original')
    ax2.plot(rolmean, color='red', label='Rolling Mean')
    ax2.plot(rolstd, color='black', label='Rolling STD')

    ax2.set_xlabel("Date")
    ax2.set_ylabel("GDP")
    ax2.legend(loc='best')
    st.write(fig2)

    """
    DICKEY FULLER TEST TAKES A LONG TIME TO RUN
    st.write("Dickey-Fuller Test: ")
    dftest = adfuller(indexedDataset['GDP'], autolag='AIC')

    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags used', 'Number of Observations Used'])
    for key, value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key] = value

    print(dfoutput)
    """