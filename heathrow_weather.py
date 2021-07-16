import os
import numpy as np
import pandas as pd

import streamlit as st

import sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor

from sklearn import preprocessing

def main():
    weather_df = pd.read_csv('heathrow_data_removed_nulls.csv')
    st.write(weather_df.head())
    st.write(weather_df.columns)
    st.write(weather_df.shape)
    st.write(weather_df.describe())

    st.write(round(100*(weather_df.isnull().sum()/len(weather_df.index)),2))

    weather_df.loc[weather_df['rain']>=40, 'Recip Type'] = 1
    weather_df.loc[weather_df['rain'] < 40, 'Recip Type'] = 0

    weather_df.loc[weather_df['sun'] >= 60, 'Sun Type'] = 1
    weather_df.loc[weather_df['sun'] < 60, 'Sun Type'] = 0

    weather_df_num = weather_df[list(weather_df.dtypes[weather_df.dtypes!='objects'].index)]

    weather_y = weather_df_num.pop('tmax')
    weather_X = weather_df_num

    train_X,test_X,train_y,test_y = train_test_split(weather_X, weather_y, test_size=0.2, random_state=4)

    st.write("LINEAR REGRESSION")
    model = LinearRegression()
    model.fit(train_X, train_y)

    prediction = model.predict(test_X)
    st.write(prediction)

    st.write(np.mean((prediction-test_y)**2))

    res = pd.DataFrame({'actual': test_y,
                        'prediction' : prediction,
                        'diff': (test_y - prediction)})

    st.write(res)

    st.write("RANDOM FOREST")

    st.write("USING MAX DEPTH OF 5")

    regr3 = RandomForestRegressor(max_depth=5, random_state=0, n_estimators=100)
    regr3.fit(train_X, train_y)
    prediction4 = regr3.predict(test_X)

    st.write(prediction4)
    st.write(np.mean((prediction4 - test_y) ** 2))

    res4 = pd.DataFrame({'actual': test_y,
                         'prediction': prediction4,
                         'diff': (test_y - prediction4)})

    st.write(res4)

    st.write("USING MAX DEPTH OF 10")

    regr = RandomForestRegressor(max_depth=10, random_state=0, n_estimators=100)
    regr.fit(train_X, train_y)
    prediction2 = regr.predict(test_X)

    st.write(prediction2)
    st.write(np.mean((prediction2 - test_y) ** 2))

    res2 = pd.DataFrame({'actual': test_y,
                        'prediction': prediction2,
                        'diff': (test_y - prediction2)})

    st.write(res2)

    st.write("USING MAX DEPTH OF 50")
    regr2 = RandomForestRegressor(max_depth=50, random_state=0, n_estimators=100)
    regr2.fit(train_X, train_y)
    prediction3 = regr2.predict(test_X)

    st.write(prediction3)
    st.write(np.mean((prediction3 - test_y) ** 2))

    res3 = pd.DataFrame({'actual': test_y,
                         'prediction': prediction3,
                         'diff': (test_y - prediction3)})

    st.write(res3)

    st.write("DECISION TREE REGRESSOR")
    regressor = DecisionTreeRegressor(random_state=0)
    regressor.fit(train_X, train_y)
