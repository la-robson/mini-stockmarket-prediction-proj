# import libraries
import pandas as pd
pd.options.display.float_format = '{:,.2f}'.format
import numpy as np
np.random.seed(seed=16)
print('Libraries imported.')

# define variables
sample_data_path = '../basic_data_cleaning/data/original_data/noaa_icoads_2012_sample.csv'
data_save_path = f'../basic_data_cleaning/data/validation_data/'

# import data
sample_df = pd.read_csv(sample_data_path)

# make dataframe of missing values
nan_df = sample_df.isnull().sum(axis=0)
perc_nan = nan_df.sea_surface_temp/len(sample_df)
print(f'\nPercent of missing values in sample data: {perc_nan*100}%')

# remove all missing values and reset the index
dropna_df = sample_df.dropna().reset_index(drop=True)

# create copy with random data dropout with same proportion of missing data as original
fakena_df = dropna_df.copy()
length = len(dropna_df)
n_nan = int(perc_nan*length)    # number of points to drop
idx_replace = np.random.randint(0, length-1, n_nan)
fakena_df.loc[idx_replace, 'sea_surface_temp'] = np.nan

# save as csv
dropna_df.to_csv(''.join([data_save_path, 'validation.csv']))
fakena_df.to_csv(''.join([data_save_path, 'test.csv']))
print(f'Saved validation.csv and test.csv')



