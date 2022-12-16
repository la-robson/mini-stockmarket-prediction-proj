# import libraries
import os
import numpy as np
from sklearn.metrics import mean_squared_error
import pandas as pd
pd.options.display.float_format = '{:,.2f}'.format
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import matplotlib.pyplot as plt
import seaborn as sns

from data_cleaning import (
drop_nan,
fill_mean,
fill_mean_chron,
fill_mean_loc
)

print('Libraries imported.')


# define functions


# define variables
sample_data_path = '../basic_data_cleaning/data/original_data/noaa_icoads_2012_sample.csv'
validation_data_path = f'../basic_data_cleaning/data/validation_data/'
validation_files = os.listdir(validation_data_path)

print('Validation data files in directory: ')
for file in validation_files:
    print('\t', file)


# import data
test_df = pd.read_csv(''.join([validation_data_path, validation_files[0]]))
validation_df = pd.read_csv(''.join([validation_data_path, validation_files[1]]))

# sort data chronologically
test_df.sort_values(by=['month', 'day', 'hour'], inplace=True)
validation_df.sort_values(by=['month', 'day', 'hour'], inplace=True)  # sort chronologically

# apply cleaning methods
drop_nan_df = drop_nan(test_df, save=False)
fill_mean_df = fill_mean(test_df, save=False)
fill_mean_chron_df = fill_mean_chron(test_df, save=False)
fill_mean_loc_df = fill_mean_loc(test_df, save=False, window=300)

# calculate MSE
base_mse = mean_squared_error(validation_df.sea_surface_temp, fill_mean_df.sea_surface_temp)
chron_mse = mean_squared_error(validation_df.sea_surface_temp, fill_mean_chron_df.sea_surface_temp)
loc_mse = mean_squared_error(validation_df.sea_surface_temp, fill_mean_loc_df.sea_surface_temp)

# plot results
sns.kdeplot(x=validation_df.sea_surface_temp, y=fill_mean_df.sea_surface_temp)
plt.show()

sns.kdeplot(x=validation_df.sea_surface_temp, y=fill_mean_chron_df.sea_surface_temp)
plt.show()

sns.kdeplot(x=validation_df.sea_surface_temp, y=fill_mean_loc_df.sea_surface_temp,)
            #fill=True, thresh=0, levels=100, cmap="mako",)
plt.show()

sns.scatterplot(x=validation_df.sea_surface_temp, y=fill_mean_loc_df.sea_surface_temp)
plt.show()

# report mean squared errors
print(f'Baseline MSE\t{base_mse}')
print(f'Chronological MSE\t{chron_mse}')
print(f'Location MSE\t{loc_mse}')

# time?