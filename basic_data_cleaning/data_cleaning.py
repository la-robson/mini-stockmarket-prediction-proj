# import libraries
import pandas as pd
pd.options.display.float_format = '{:,.2f}'.format
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print('Libraries imported.')


# define functions
def save_df(df, name):
    df.to_csv(''.join([data_save_path, name]))
    print(f'Saved: {name}')

# define variables
sample_data_path = '../basic_data_cleaning/data/original_data/noaa_icoads_2012_sample.csv'
data_save_path = f'../basic_data_cleaning/data/cleaned_data/'
n = 5000    # sample size

# import data
sample_df = pd.read_csv(sample_data_path)


# data removal
dropped_nan_df = sample_df.dropna()
save_df(dropped_nan_df, 'dropped_missing_sample.csv')

# fill with mean
mean_fill_df = sample_df.copy()
mean_fill_df["sea_surface_temp"] = mean_fill_df["sea_surface_temp"].replace(np.NaN, mean_fill_df["sea_surface_temp"].mean())
save_df(mean_fill_df, 'mean_fill_sample.csv')

# improve mean fill to be chronologically implemented
mean_fill_df2 = sample_df.copy()
mean_fill_df2.sort_values(by=['month', 'day', 'hour'], inplace=True)    # sort chronologically
curr_df = mean_fill_df2.head(1) # initialize current df with first row

# iterate through each row in dataset (equivalent to receiving stream of data)
for i in range(1, len(mean_fill_df2)):
    # get dataset so far
    curr_df = curr_df.append(mean_fill_df2.iloc[i])
    # if missing value fill with the mean of the dataset available so far
    if np.isnan(curr_df.sea_surface_temp.iloc[i]):
        curr_df.sea_surface_temp.iloc[i] = curr_df.sea_surface_temp.mean()

save_df(curr_df, 'mean_fill_2_sample.csv')

