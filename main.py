# import required libraries
import os
import pandas as pd
from data_processes import (
    import_stockdata,
    split_xy,
)

def main():
    # get tesla stock data
    tesla_filepath = ''.join([os.getcwd(), "/data/tesla.csv"])
    df = import_stockdata(tesla_filepath)
    print(df.head())
    X_train, X_test, y_train, y_test = split_xy(df=df, x_vars=['Open'], y_var=['Close'])
    print(X_train.head())
    print(y_train.head())


if __name__ == "__main__":
    main()
