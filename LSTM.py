# import keras libraries to make LSTM network
from keras.models import Sequential
from keras.layers import (
    Dense,
    LSTM,
    Dropout,
)

def initialise_lstm_network(X_train_shape):
    """
    Make a Recurrent Neural Network (RNN) with long short-term memory layers
    :param X_train_shape:
    :return regressor: return network
    """
    regressor = Sequential()
    # add first LSTM layer with dropout regularisation
    regressor.add(LSTM(units=50, return_sequences=True, input_shape=(X_train_shape, 1)))
    regressor.add(Dropout(0.2))
    # add 3 more LSTM layers with dropout regularisation
    regressor.add(LSTM(units=50, return_sequences=True))
    regressor.add(Dropout(0.2))
    regressor.add(LSTM(units=50, return_sequences=True))
    regressor.add(Dropout(0.2))
    regressor.add(LSTM(units=50))
    regressor.add(Dropout(0.2))
    # add dense output layer
    regressor.add(Dense(units=1))
    # compile the RNN
    regressor.compile(optimizer='adam', loss='mean_squared_error')

    return regressor