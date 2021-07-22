import getinput
import fypconnect

import os
import numpy as np
import pandas as pd

import streamlit as st
from matplotlib import pyplot as plt

import sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import PolynomialFeatures

global train_X,test_X,train_y,test_y

def main():
    weather_df = pd.read_csv('heathrow_data_removed_nulls.csv')
    #st.write(weather_df.head())
    #st.write(weather_df.columns)
    #st.write(weather_df.shape)
    #st.write(weather_df.describe())

    #st.write(round(100*(weather_df.isnull().sum()/len(weather_df.index)),2))

    weather_df.loc[weather_df['rain']>=40, 'Recip Type'] = 1
    weather_df.loc[weather_df['rain'] < 40, 'Recip Type'] = 0

    weather_df.loc[weather_df['sun'] >= 60, 'Sun Type'] = 1
    weather_df.loc[weather_df['sun'] < 60, 'Sun Type'] = 0

    weather_df_num = weather_df[list(weather_df.dtypes[weather_df.dtypes!='objects'].index)]

    weather_y = weather_df_num.pop('tmax')
    weather_X = weather_df_num

    train_X,test_X,train_y,test_y = train_test_split(weather_X, weather_y, test_size=0.2, random_state=4)

    #Choose ML Method
    st.write("Please choose a method of Machine Learning*:")
    st.write("*(Polynomial Regression takes a while to run)")
    task = st.selectbox("ML Methods", ["LINEAR REGRESSION", "RANDOM FOREST", "DECISION TREE REGRESSOR", "POLYNOMIAL REGRESSION"])
    if task == "LINEAR REGRESSION":
        linear(train_X,test_X,train_y,test_y)
    if task == "RANDOM FOREST":
        rand(train_X,test_X,train_y,test_y)
    if task == "DECISION TREE REGRESSOR":
        desc(train_X,test_X,train_y,test_y)
    if task == "POLYNOMIAL REGRESSION":
        poly(train_X, test_X, train_y, test_y)

    #else:
        #st.warning("PLEASE SELECT A MACHINE LEARNING METHOD")

###############################################################################################

def linear(train_X,test_X,train_y,test_y):
    st.write("LINEAR REGRESSION")
    model = LinearRegression()
    model.fit(train_X, train_y)

    pred_linear = model.predict(test_X)
    # st.write(pred_linear)

    err = np.mean((pred_linear - test_y) ** 2)
    out_err = ("{0:.3%}".format(err))
    st.write(f"Error rate: {out_err}")

    """
    plt.figure(figsize=(4,3))
    plt.scatter(test_y, pred_linear)
    plt.plot([0, 100], [0, 100], '--k')
    plt.axis('tight')
    plt.xlabel('True')
    plt.ylabel('Predicted')
    plt.tight_layout()
    """

    res = pd.DataFrame({'actual': test_y,
                        'pred_linear': pred_linear,
                        'diff': (test_y - pred_linear)})

    # st.write(res)

    user_input_given = getinput.get_heathrow_input()
    user_pred = model.predict(user_input_given)
    st.write(f"Predicted Max Temperature for given inputs (degrees C): {user_pred}")

###############################################################################################

def rand(train_X,test_X,train_y,test_y):
    st.write("RANDOM FOREST")

    st.write("Please choose the maximum depth of the Random Forest:")
    task = st.selectbox("Depths", ["5", "10", "50"])
    if task == "5":
        rand_5(train_X,test_X,train_y,test_y)
    if task == "10":
        rand_10(train_X,test_X,train_y,test_y)
    if task == "50":
        rand_50(train_X,test_X,train_y,test_y)

def rand_5(train_X,test_X,train_y,test_y):
    st.write("USING MAX DEPTH OF 5")

    regr_RF_depth_5 = RandomForestRegressor(max_depth=5, random_state=0, n_estimators=100)
    regr_RF_depth_5.fit(train_X, train_y)
    pred_RF_depth_5 = regr_RF_depth_5.predict(test_X)

    # st.write(pred_RF_depth_5)
    err_5 = np.mean((pred_RF_depth_5 - test_y) ** 2)
    out_err_5 = ("{0:.3%}".format(err_5))
    st.write(f"Error rate: {out_err_5}")

    res_depth_5 = pd.DataFrame({'actual': test_y,
                                'pred_RF': pred_RF_depth_5,
                                'diff': (test_y - pred_RF_depth_5)})

    # st.write(res_depth_5)

    user_input_given = getinput.get_heathrow_input()
    user_pred = regr_RF_depth_5.predict(user_input_given)
    st.write(f"Predicted Max Temperature for given inputs (degrees C): {user_pred}")

def rand_10(train_X,test_X,train_y,test_y):
    st.write("USING MAX DEPTH OF 10")

    regr_RF_depth_10 = RandomForestRegressor(max_depth=10, random_state=0, n_estimators=100)
    regr_RF_depth_10.fit(train_X, train_y)
    pred_RF_depth_10 = regr_RF_depth_10.predict(test_X)

    # st.write(pred_RF_depth_10)
    err_10 = np.mean((pred_RF_depth_10 - test_y) ** 2)
    out_err_10 = ("{0:.3%}".format(err_10))
    st.write(f"Error rate: {out_err_10}")

    res_depth_10 = pd.DataFrame({'actual': test_y,
                                 'pred_RF': pred_RF_depth_10,
                                 'diff': (test_y - pred_RF_depth_10)})

    # st.write(res_depth_10)
    user_input_given = getinput.get_heathrow_input()
    user_pred = regr_RF_depth_10.predict(user_input_given)
    st.write(f"Predicted Max Temperature for given inputs (degrees C): {user_pred}")

def rand_50(train_X,test_X,train_y,test_y):
    st.write("USING MAX DEPTH OF 50")
    regr_RF_depth_50 = RandomForestRegressor(max_depth=50, random_state=0, n_estimators=100)
    regr_RF_depth_50.fit(train_X, train_y)
    pred_RF_depth_50 = regr_RF_depth_50.predict(test_X)

    # st.write(pred_RF_depth_50)
    err_50 = np.mean((pred_RF_depth_50 - test_y) ** 2)
    out_err_50 = ("{0:.3%}".format(err_50))
    st.write(f"Error rate: {out_err_50}")

    res_depth_50 = pd.DataFrame({'actual': test_y,
                                 'pred_RF': pred_RF_depth_50,
                                 'diff': (test_y - pred_RF_depth_50)})

    # st.write(res_depth_50)
    user_input_given = getinput.get_heathrow_input()
    user_pred = regr_RF_depth_50.predict(user_input_given)
    st.write(f"Predicted Max Temperature for given inputs (degrees C): {user_pred}")

###############################################################################################

def desc(train_X,test_X,train_y,test_y):
    st.write("DECISION TREE REGRESSOR")
    regressor_DT = DecisionTreeRegressor(random_state=0)
    regressor_DT.fit(train_X, train_y)

    pred_DT = regressor_DT.predict(test_X)
    err = np.mean((pred_DT - test_y) ** 2)
    out_err = ("{0:.3%}".format(err))
    st.write(f"Error rate: {out_err}")

    res_DT = pd.DataFrame({'actual': test_y,
                           'pred_RF': pred_DT,
                           'diff': (test_y - pred_DT)})

    # st.write(res_DT)
    user_input_given = getinput.get_heathrow_input()
    user_pred = regressor_DT.predict(user_input_given)
    st.write(f"Predicted Max Temperature for given inputs (degrees C): {user_pred}")



###############################################################################################

def poly(train_X,test_X,train_y,test_y):
    poly = PolynomialFeatures(degree=4)
    X_poly = poly.fit_transform(train_X)

    poly.fit(X_poly, train_y)
    linear2 = LinearRegression()
    linear2.fit(X_poly, train_y)

    pred = linear2.predict(poly.fit_transform(test_X))
    err = np.mean((pred-test_y)**2)
    out_err = ("{0:.3%}".format(err))
    st.write(f"Error rate: {out_err}")

    user_input_given = getinput.get_heathrow_input()
    user_pred = linear2.predict(poly.fit_transform(user_input_given))
    st.write(f"Predicted Max Temperature for given inputs (degrees C): {user_pred}")
