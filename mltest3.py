import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import matplotlib.pylab as plt
from sklearn.linear_model import LinearRegression as lm

def dt_float(d):
    return d.timestamp()

def main(df, pred):
    st.write("Data frame:")
    st.write(df)
    st.write(pred)

    train = df[df["Class"] == "Train"]
    test = df[df["Class"] == "Test"]
    df = df.drop(['Class'], axis=1)

    st.write(train)
    st.write(test)

    x_train = train["Date"]
    y_train = train["gdp"]

    x_test = test["Date"]
    y_test = test["gdp"]

    y = df['gdp']
    x = df.drop(['gdp'], axis=1)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

    st.write(x_train.shape)
    st.write(y_train.shape)

    st.write(x_test.shape)
    st.write(y_test.shape)

    st.write("Train set:")
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(train['Date'], train['gdp'])
    ax.set_xlabel("Date")
    ax.set_ylabel("GDP")
    st.write(fig)

    st.write("Test set:")
    fig2 = plt.figure()
    ax2 = fig2.add_subplot(1, 1, 1)
    ax2.plot(test['Date'], test['gdp'])
    ax2.set_xlabel("Date")
    ax2.set_ylabel("GDP")
    st.write(fig2)

    st.write(type(x_train))
    model = lm().fit(x_train, y_train)
    predictions = model.predict(x_test)

    st.write("Predictions:")
    fig3 = plt.figure()
    ax3 = fig3.add_subplot(1, 1, 1)
    ax3.plot(y_test, predictions)
    ax3.set_xlabel("Predictions")
    ax3.set_ylabel("y_test")
    st.write(fig3)