import numpy as np
import pandas as pd
from datetime import datetime
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

    new_df = pd.concat([indexedDataset, indexedDataset.shift(1)], axis=1)
    new_df.columns = ['GDP', 'GDP_forecasted']

    gdp_test = new_df.iloc[1:]
    st.write(gdp_test)
    gdp_error = mean_squared_error(gdp_test.GDP, gdp_test.GDP_forecasted)
    gdp_error_sq = np.sqrt(gdp_error)
    st.write(gdp_error_sq)

    # ARIMA(p, d, q)
    st.write(plot_acf(indexedDataset)) # to identify q = 17
    st.write(plot_pacf(indexedDataset, lags=15)) # to identify p = 4

    gdp_train = indexedDataset.iloc[0:126]
    gdp_test = indexedDataset.iloc[126:]

    gdp_model = ARIMA(gdp_train.astype(int), order=(4, 1, 18))
    gdp_model_fit = gdp_model.fit(transparams=False)


    for index, row in indexedDataset.iterrows():
        row['gdp'] = int(round(row['gdp']))