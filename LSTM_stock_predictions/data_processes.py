import os
import pandas as pd
import numpy as np

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


def split_testtrain(df, var, year = 2018):
    """
    Splits dataframe into test and train data based off a year cut off value (2018 by default)
    :param df: Dataframe to be split
    :param var: Variable of interest
    :return train, test: tuple containing numpy arrays formatted to be scaled
    """
    # split data based on year condition
    train = df.loc[pd.DatetimeIndex(df['Date']).year < year]
    test = df.loc[pd.DatetimeIndex(df['Date']).year >= year]

    # get variable of interest and reshape into correct format
    train = train[var].values.reshape(-1, 1)
    test = test[var].values.reshape(-1, 1)

    return train, test


def normalise_data(df, var):
    """
    normalise the input parameters to improve model performance
    :return scaled_X_train, scaled_X_test: tuple of scaled training and test data
    """
    # get split test and train data
    train, test = split_testtrain(df, var)
    # create scalar based off training input values
    scalar = MinMaxScaler(feature_range=(0, 1))
    # apply the same scalar to the training and test data
    scaled_train = scalar.fit_transform(train)
    scaled_test = scalar.transform(test)

    return scaled_train, scaled_test, scalar


def reshape_input(scaled_data, timesteps=60):
    """
    Reshape the input data for the LSTM
    :param scaled_data: array of scaled data
    :param timesteps: number of backwards timesteps used in model
    :return X_shaped, y_shaped: tuple of input (x) and output (y) data to use with network
    """
    # empty lists to append data to
    X_shaped = []
    y_shaped = []
    # iterate through each row adding data
    for i in range(timesteps, len(scaled_data)):
        X_shaped.append(scaled_data[i - timesteps:i, 0])
        y_shaped.append(scaled_data[i, 0])
    # convert to numpy arrays
    X_shaped, y_shaped = np.array(X_shaped), np.array(y_shaped)
    # reshape
    X_shaped = np.reshape(X_shaped, (X_shaped.shape[0], X_shaped.shape[1], 1))

    return X_shaped, y_shaped
