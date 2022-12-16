# import libraries
import numpy as np
import pandas as pd

pd.options.display.float_format = '{:,.2f}'.format
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

print('Libraries imported.')


# define functions
def save_df(df, name):
    df.to_csv(''.join([data_save_path, name]))
    print(f'Saved: {name}')


# data removal
def drop_nan(df, filename='dropped_missing.csv', save=True):
    dropped_nan_df = df.dropna()
    if save:
        save_df(dropped_nan_df, filename)
    return dropped_nan_df


# fill with mean
def fill_mean(df, filename='fill_mean.csv', variable="sea_surface_temp", save=True):
    '''

    '''
    mean_fill_df = df.copy()
    mean_fill_df[variable] = mean_fill_df[variable].replace(np.NaN, mean_fill_df[variable].mean())
    if save:
        save_df(mean_fill_df, filename)
    return mean_fill_df


# improve mean fill to be chronologically implemented
def fill_mean_chron(df, filename='chron_mean_fill.csv', variable="sea_surface_temp", save=True):
    """
    df must be already sorted chronologically
    """
    df.sort_values(by=['month', 'day', 'hour'], inplace=True)  # sort chronologically
    print(df.head())
    curr_df = df.head(1)  # initialize current df with first row


    # iterate through each row in dataset (equivalent to receiving stream of data)
    for i in range(1, len(df)):
        # get dataset so far
        curr_df = curr_df.append(df.iloc[i])
        # if missing value fill with the mean of the dataset available so far
        if np.isnan(curr_df.iloc[i][variable]):
            curr_df[variable].iloc[i] = curr_df[variable].mean()
    # save csv and return dataframe
    if save:
        save_df(curr_df, filename)
    return curr_df


# improve mean fill to be chronologically implemented
def fill_mean_loc(df, filename='loc_mean_fill.csv', variable="sea_surface_temp", save=True, window=3):
    """
    df must be already sorted chronologically
    """
    n = len(df)
    df.sort_values(by=['longitude', 'latitude'], inplace=True) # sort by location
    print(df.head(20))
    # iterate through each row in dataset
    if window >= len(df):
        print(f'Invalid window selected, must be less that data length {n}')
    for i in range(0, len(df)):
        # if missing value fill with the mean of the geographically adjacent values
        if np.isnan(df.iloc[i][variable]):
            if i-window < 0:
                df.loc[:, variable].iloc[i] = np.nanmean(df[variable].iloc[0:i+window+1])
            elif i+window+1 > len(df):
                df.loc[:, variable].iloc[i] = np.nanmean(df[variable].iloc[i-window:n])
            else:
                df.loc[:, variable].iloc[i] = np.nanmean(df[variable].iloc[i-window:i+window+1])

    # save csv and return dataframe
    if save:
        save_df(df, filename)
    return df


if __name__ == "__main__":
    # define variables
    sample_data_path = '../basic_data_cleaning/data/original_data/noaa_icoads_2012_sample.csv'
    data_save_path = f'../basic_data_cleaning/data/cleaned_data/'

    # import data
    sample_df = pd.read_csv(sample_data_path)
    # sample_df.sort_values(by=['month', 'day', 'hour'], inplace=True)  # sort chronologically
    print(sample_df.head())
    # clean sample data
    drop_nan(sample_df.copy(), 'dropped_missing_sample.csv')
    fill_mean(sample_df.copy(), 'mean_fill_sample.csv')
    fill_mean_loc(sample_df.copy(), 'loc_mean_fill_sample.csv')
    fill_mean_chron(sample_df.copy(), 'chron_mean_fill_sample.csv')  # df must be chronologically sorted first

