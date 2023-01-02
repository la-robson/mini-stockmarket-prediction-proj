# import required libraries
import os
import pandas as pd
from data_processes import (
    import_stockdata,
    normalise_data,
    reshape_input
)
import matplotlib.pyplot as plt
from LSTM import initialise_lstm_network


def main():
    # get tesla stock data
    tesla_filepath = ''.join([os.getcwd(), "/data/tesla.csv"])
    df = import_stockdata(tesla_filepath)

    # define relevent variables
    price_var = 'Open'
    timesteps = 60
    epochs = 20
    batch_size = 32

    # select data of interest and normalise
    scaled_train, scaled_test, scalar = normalise_data(df, price_var)

    # reshape data into appropriate format for LSTM
    X_train, y_train = reshape_input(scaled_train, timesteps=timesteps)
    X_test, y_test = reshape_input(scaled_test, timesteps=timesteps)



    # create RNN
    network = initialise_lstm_network(X_train_shape=X_train.shape[1])
    # fit to training data
    network.fit(X_train, y_train, epochs=epochs, batch_size=batch_size)
    # get predictions for closing stock price based on x_test data
    y_predicted = network.predict(X_test)
    price_predicted = scalar.inverse_transform(y_predicted)


    # compare prediction with actual value
    # reformat data
    plot_df = df[['Date', price_var]]
    plot_df = plot_df.loc[pd.DatetimeIndex(df['Date']).year >= 2018].tail(len(price_predicted))
    plot_df['pred_open'] = price_predicted
    # save as csv
    plot_df.to_csv('prediction.csv')
    # Visualise results
    plt.plot(plot_df['Date'], plot_df[price_var], color='red', label='Predicted')
    plt.plot(plot_df['Date'], plot_df['pred_open'], color='black', label='Actual')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
