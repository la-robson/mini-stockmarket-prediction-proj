import os
import pandas as pd

from sklearn.preprocessing import MinMaxScaler


def import_stockdata(filepath):
    """
    Import csv file as a dataframe
    :param filepath: path to stocks datafile
    :return df: dataframe of stocks file
    """
    df = pd.read_csv(filepath)
    # convert date to datetime format
    df.Date = pd.to_datetime(df.Date, format='%d-%m-%Y')
    return df

def split_xy(df, x_vars, y_var):
    train = df.loc[pd.DatetimeIndex(df['Date']).year >= 2018]
    test = df.loc[pd.DatetimeIndex(df['Date']).year < 2018]
    X_train = train[x_vars]
    y_train = train[y_var]
    X_test = train[x_vars]
    y_test = test[y_var]
    return X_train, X_test, y_train, y_test

def normalise_data(X):
    """
    normalise the dataset
    :return:
    """
    scalar = MinMaxScaler(feature_range=(0,1))
    scaled_X = scalar.fit_transform(X)

    return scaled_X
