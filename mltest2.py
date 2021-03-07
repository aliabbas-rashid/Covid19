import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pylab as plt
from matplotlib import pyplot
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.ar_model import AutoReg
from math import sqrt

# Create a difference transform of the data set
def difference(ds):
    diff = list()
    for i in range(1, len(ds)):
        value = ds[i] - ds[i -1]
        diff.append(value)
    return diff

# Make a prediction (give regression coefficients and lag obs)
def predict(coef, h):
    yhat = coef[0]
    for i in range(1, len(coef)):
        yhat += coef[i] * h[-i]
    return yhat

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
    #ax2.plot(rolstd, color='black', label='Rolling STD')

    ax2.set_xlabel("Date")
    ax2.set_ylabel("GDP")
    ax2.legend(loc='best')
    st.write(fig2)

    new_df = pd.concat([indexedDataset, indexedDataset.shift(1)], axis=1)
    new_df.columns = ['GDP', 'GDP_forecasted']

    gdp_test = new_df.iloc[1:]
    st.write(gdp_test.head())
    gdp_error = mean_squared_error(gdp_test.GDP, gdp_test.GDP_forecasted)
    gdp_error_sq = np.sqrt(gdp_error)
    st.write(gdp_error_sq)

    gdp_train = indexedDataset.iloc[1:126]
    gdp_test = indexedDataset.iloc[126:]

    model = AutoReg(gdp_train.astype(float), lags=6)
    model_fit = model.fit()
    coef = model_fit.params
    st.write(gdp_train)

    history = [gdp_train[i] for i in range(len(gdp_train))]
    predictions = list()
    for t in range(len(gdp_test)):
        yhat = predict(coef, history)
        obs = gdp_test[t]
        predictions.append(yhat)
        history.append(obs)

    rsme = sqrt(mean_squared_error(gdp_test, predictions))

    st.write(f"Test RSME: {rsme}.3f")
