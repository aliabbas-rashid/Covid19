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

    ###############################################################################################

    st.write("LINEAR REGRESSION")
    model = LinearRegression()
    model.fit(train_X, train_y)

    pred_linear = model.predict(test_X)
    st.write(pred_linear)

    st.write(np.mean((pred_linear-test_y)**2))

    res = pd.DataFrame({'actual': test_y,
                        'pred_linear' : pred_linear,
                        'diff': (test_y - pred_linear)})

    st.write(res)

    ###############################################################################################

    st.write("RANDOM FOREST")

    st.write("USING MAX DEPTH OF 5")

    regr_RF_depth_5 = RandomForestRegressor(max_depth=5, random_state=0, n_estimators=100)
    regr_RF_depth_5.fit(train_X, train_y)
    pred_RF_depth_5 = regr_RF_depth_5.predict(test_X)

    st.write(pred_RF_depth_5)
    st.write(np.mean((pred_RF_depth_5 - test_y) ** 2))

    res_depth_5 = pd.DataFrame({'actual': test_y,
                         'pred_RF': pred_RF_depth_5,
                         'diff': (test_y - pred_RF_depth_5)})

    st.write(res_depth_5)

    ###############################################################################################

    st.write("USING MAX DEPTH OF 10")

    regr_RF_depth_10 = RandomForestRegressor(max_depth=10, random_state=0, n_estimators=100)
    regr_RF_depth_10.fit(train_X, train_y)
    pred_RF_depth_10 = regr_RF_depth_10.predict(test_X)

    st.write(pred_RF_depth_10)
    st.write(np.mean((pred_RF_depth_10 - test_y) ** 2))

    res_depth_10 = pd.DataFrame({'actual': test_y,
                        'pred_RF': pred_RF_depth_10,
                        'diff': (test_y - pred_RF_depth_10)})

    st.write(res_depth_10)

    ###############################################################################################

    st.write("USING MAX DEPTH OF 50")
    regr_RF_depth_50 = RandomForestRegressor(max_depth=50, random_state=0, n_estimators=100)
    regr_RF_depth_50.fit(train_X, train_y)
    pred_RF_depth_50 = regr_RF_depth_50.predict(test_X)

    st.write(pred_RF_depth_50)
    st.write(np.mean((pred_RF_depth_50 - test_y) ** 2))

    res_depth_50 = pd.DataFrame({'actual': test_y,
                         'pred_RF': pred_RF_depth_50,
                         'diff': (test_y - pred_RF_depth_50)})

    st.write(res_depth_50)

    ###############################################################################################

    st.write("DECISION TREE REGRESSOR")
    regressor_DT = DecisionTreeRegressor(random_state=0)
    regressor_DT.fit(train_X, train_y)

    pred_DT = regressor_DT.predict(test_X)
    st.write(np.mean((pred_DT - test_y) ** 2))

    res_DT = pd.DataFrame({'actual': test_y,
                                 'pred_RF': pred_DT,
                                 'diff': (test_y - pred_DT)})

    st.write(res_DT)
