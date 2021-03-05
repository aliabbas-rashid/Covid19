from sklearn import model_selection
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import numpy as np
import streamlit as st
import pandas as pd

def main(df, pred):

    # Split date into year, month, day etc...
    df['Date'] = pd.to_datetime(df['Date'])
    df['Date'] = df['Date'].dt.strftime('%m.%d.%Y')
    df['year'] = pd.DatetimeIndex(df['Date']).year
    df['month'] = pd.DatetimeIndex(df['Date']).month
    df['day'] = pd.DatetimeIndex(df['Date']).day
    df['dayofyear'] = pd.DatetimeIndex(df['Date']).dayofyear
    df['weekofyear'] = pd.DatetimeIndex(df['Date']).weekofyear
    df['weekday'] = pd.DatetimeIndex(df['Date']).weekday
    df['quarter'] = pd.DatetimeIndex(df['Date']).quarter
    df['is_month_start'] = pd.DatetimeIndex(df['Date']).is_month_start
    df['is_month_end'] = pd.DatetimeIndex(df['Date']).is_month_end

    df = df.drop(['Date'], axis=1)

    # Dummy encoding
    df = pd.get_dummies(df, columns=['year'], drop_first=True, prefix='year')

    df = pd.get_dummies(df, columns=['month'], drop_first=True, prefix='month')

    df = pd.get_dummies(df, columns=['weekday'], drop_first=True, prefix='wday')
    df = pd.get_dummies(df, columns=['quarter'], drop_first=True, prefix='qrtr')

    df = pd.get_dummies(df, columns=['is_month_start'], drop_first=True, prefix='m_start')

    df = pd.get_dummies(df, columns=['is_month_end'], drop_first=True, prefix='m_end')

    # Grab the train and test data
    train = df[df["Class"] == "Train"]
    test = df[df["Class"] == "Test"]

    # Drop train and test columns
    train = train.drop(['Class'], axis=1)
    test = test.drop(['Class'], axis=1)

    # Grab train data values
    target_column_train = ['gdp']
    predictors_train = list(set(list(train.columns)) - set(target_column_train))

    X_train = train[predictors_train].values
    y_train = train[target_column_train].values

    # Grab test data values
    target_column_test = ['gdp']
    predictors_test = list(set(list(test.columns)) - set(target_column_test))

    X_test = test[predictors_test].values
    y_test = test[target_column_test].values

    # Descision Tree (Regressor)
    dtree = DecisionTreeRegressor(max_depth=8, min_samples_leaf=0.13, random_state=3)
    dtree.fit(X_train, y_train)

    # Predictions for decision tree on the train data
    pred_train_tree = dtree.predict(X_train)
    st.write(np.sqrt(mean_squared_error(y_train, pred_train_tree)))
    st.write(r2_score(y_train, pred_train_tree))

    # Predictions for decision tree on the test data
    pred_test_tree = dtree.predict(X_test)
    st.write(np.sqrt(mean_squared_error(y_test, pred_test_tree)))
    st.write(r2_score(y_test, pred_test_tree))

######################################################################################
    # Fit the regression tree 'dtree1' and 'dtree2' with different max depths for testing
    dtree1 = DecisionTreeRegressor(max_depth=2)
    dtree2 = DecisionTreeRegressor(max_depth=5)
    dtree1.fit(X_train, y_train)
    dtree2.fit(X_train, y_train)

    # Predictions for decision tree 1 and 2 on the train data
    tr1 = dtree1.predict(X_train)
    tr2 = dtree2.predict(X_train)

    # Predictions for decision tree 1 and 2 on the test data
    y1 = dtree1.predict(X_test)
    y2 = dtree2.predict(X_test)

    # Print root-mean-square-error and R-squared value for regression tree 1 on training data
    st.write("RMSE and R-squared value for regression tree 1 on training data")
    st.write(np.sqrt(mean_squared_error(y_train, tr1)))
    st.write(r2_score(y_train, tr1))

    # Print root-mean-square-error and R-squared value for regression tree 1 on testing data
    st.write("RMSE and R-squared value for regression tree 1 on testing data")
    st.write(np.sqrt(mean_squared_error(y_test, y1)))
    st.write(r2_score(y_test, y1))

    # Print root-mean-square-error and R-squared value for regression tree 2 on training data
    st.write("RMSE and R-squared value for regression tree 2 on training data")
    st.write(np.sqrt(mean_squared_error(y_train, tr2)))
    st.write(r2_score(y_train, tr2))

    # Print root-mean-square-error and R-squared value for regression tree 2 on testing data
    st.write("RMSE and R-squared value for regression tree 2 on testing data")
    st.write(np.sqrt(mean_squared_error(y_test, y2)))
    st.write(r2_score(y_test, y2))

    # Build regressor tree
    # Random Forest model
    model_rf = RandomForestRegressor(n_estimators=5000, oob_score=True, random_state=100)
    model_rf.fit(X_train, y_train)
    pred_train_rf = model_rf.predict(X_train)
    st.write("----")
    st.write("Random forest regressor RMSE and R-squared value for train set")
    st.write(np.sqrt(mean_squared_error(y_train, pred_train_rf)))
    st.write(r2_score(y_train, pred_train_rf))

    pred_test_rf = model_rf.predict(X_test)
    st.write("Random forest regressor RMSE and R-squared value for test set")
    st.write(np.sqrt(mean_squared_error(y_test, pred_test_rf)))
    st.write(r2_score(y_test, pred_test_rf))

    # Predictions on user input data
    pred['Date'] = pd.to_datetime(pred['Date'])
    pred['Date'] = df['Date'].dt.strftime('%m.%d.%Y')
    pred['year'] = pd.DatetimeIndex(pred['Date']).year
    pred['month'] = pd.DatetimeIndex(pred['Date']).month
    pred['day'] = pd.DatetimeIndex(pred['Date']).day
    pred['dayofyear'] = pd.DatetimeIndex(pred['Date']).dayofyear
    pred['weekofyear'] = pd.DatetimeIndex(pred['Date']).weekofyear
    pred['weekday'] = pd.DatetimeIndex(pred['Date']).weekday
    pred['quarter'] = pd.DatetimeIndex(pred['Date']).quarter
    pred['is_month_start'] = pd.DatetimeIndex(pred['Date']).is_month_start
    pred['is_month_end'] = pd.DatetimeIndex(pred['Date']).is_month_end

    pred = pred.drop(['Date'], axis=1)

    # Dummy encoding
    pred = pd.get_dummies(pred, columns=['year'], drop_first=True, prefix='year')

    pred = pd.get_dummies(pred, columns=['month'], drop_first=True, prefix='month')

    pred = pd.get_dummies(pred, columns=['weekday'], drop_first=True, prefix='wday')
    pred = pd.get_dummies(pred, columns=['quarter'], drop_first=True, prefix='qrtr')

    pred = pd.get_dummies(pred, columns=['is_month_start'], drop_first=True, prefix='m_start')

    pred = pd.get_dummies(pred, columns=['is_month_end'], drop_first=True, prefix='m_end')

    #user_predict = model_rf.predict(predict)
    #st.write(user_predict)