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
    fill_mean_chron_win,
    fill_mean_loc
)

print('Libraries imported.')

# define functions


# define variables
sample_data_path = '../basic_data_cleaning/data/original_data/noaa_icoads_2012_sample.csv'
validation_data_path = f'../basic_data_cleaning/data/validation_data/'
validation_files = os.listdir(validation_data_path)
plot_save_path = f'../basic_data_cleaning/data/clean_comparison_plots/'

print('Validation data files in directory: ')
for file in validation_files:
    print('\t', file)

# import data
test_df = pd.read_csv(''.join([validation_data_path, validation_files[0]]))
val_df = pd.read_csv(''.join([validation_data_path, validation_files[1]]))

# for some reason the sorts are not working properly in the cleaning functions so sort again here
chron_sort_t_df = test_df.sort_values(by=['month', 'day', 'hour'])
chron_sort_v_df = val_df.sort_values(by=['month', 'day', 'hour'])
loc_sort_t_df = test_df.sort_values(by=['longitude', 'latitude'])
loc_sort_v_df = val_df.sort_values(by=['longitude', 'latitude'])
# apply cleaning methods
drop_nan_df = drop_nan(test_df, save=False)
fill_mean_df = fill_mean(test_df, save=False)
fill_mean_chron_df = fill_mean_chron(chron_sort_t_df, save=False)
fill_mean_chron_win_df = fill_mean_chron_win(chron_sort_t_df, save=False, window=30)
fill_mean_loc_df = fill_mean_loc(loc_sort_t_df, save=False, window=300)

# calculate MSE
base_mse = round(mean_squared_error(val_df.sea_surface_temp, fill_mean_df.sea_surface_temp), 3)
chron_mse = round(mean_squared_error(chron_sort_v_df.sea_surface_temp, fill_mean_chron_df.sea_surface_temp), 3)
chron_win_mse = round(mean_squared_error(chron_sort_v_df.sea_surface_temp, fill_mean_chron_win_df.sea_surface_temp), 3)
loc_mse = round(mean_squared_error(loc_sort_v_df.sea_surface_temp, fill_mean_loc_df.sea_surface_temp), 3)

# plot results
plot1 = sns.kdeplot(x=val_df.sea_surface_temp, y=fill_mean_df.sea_surface_temp)
plot1.set(xlabel="Validation temperature (°C)", ylabel="Cleaned data (°C)",
          title=f'Mean fill MSE={base_mse}')
plt.savefig(''.join([plot_save_path, 'mean_fill.png']))
plt.show()

plot2 = sns.kdeplot(x=chron_sort_v_df.sea_surface_temp, y=fill_mean_chron_df.sea_surface_temp)
plot2.set(xlabel="Validation temperature (°C)", ylabel="Cleaned data (°C)",
          title=f'Chronological mean fill MSE={chron_mse}')
plt.savefig(''.join([plot_save_path, 'chron_mean_fill.png']))
plt.show()

plot3 = sns.kdeplot(x=chron_sort_v_df.sea_surface_temp, y=fill_mean_chron_win_df.sea_surface_temp)
plot3.set(xlabel="Validation temperature (°C)", ylabel="Cleaned data (°C)",
          title=f'Chronological mean fill with window MSE={chron_win_mse}')
plt.savefig(''.join([plot_save_path, 'chron_mean_window_fill.png']))
plt.show()

plot4 = sns.kdeplot(x=loc_sort_v_df.sea_surface_temp, y=fill_mean_loc_df.sea_surface_temp, )
plot4.set(xlabel="Validation temperature (°C)", ylabel="Cleaned data (°C)",
          title=f'Location mean fill with window MSE={loc_mse}')
plt.savefig(''.join([plot_save_path, 'loc_mean_fill.png']))
plt.show()

# report mean squared errors
print(f'Baseline MSE\t{base_mse}')
print(f'Chronological MSE\t{chron_mse}')
print(f'Chronological windowed MSE\t{chron_win_mse}')
print(f'Location MSE\t{loc_mse}')

# TODO: time them to compare efficiency
