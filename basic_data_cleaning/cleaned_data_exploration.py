# import libraries
import pandas as pd
pd.options.display.float_format = '{:,.2f}'.format
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print('Libraries imported.')


# define functions


# define variables
sample_data_path = '../basic_data_cleaning/data/original_data/noaa_icoads_2012_sample.csv'
cleaned_data_path = f'../basic_data_cleaning/data/cleaned_data/'
cleaned_files = os.listdir(cleaned_data_path)

print('Cleaned data files in directory: ')
for file in cleaned_files:
    print('\t', file)


# import data
sample_df = pd.read_csv(sample_data_path)
dropped_df = pd.read_csv(''.join([cleaned_data_path, cleaned_files[0]]))
meanfill2_df = pd.read_csv(''.join([cleaned_data_path, cleaned_files[1]]))
meanfill_df = pd.read_csv(''.join([cleaned_data_path, cleaned_files[2]]))

# rename columns
dropped_df.rename(columns={"sea_surface_temp": "sea_surface_temp_drop"}, inplace=True)
meanfill_df.rename(columns={"sea_surface_temp": "sea_surface_temp_mean"}, inplace=True)
meanfill2_df.rename(columns={"sea_surface_temp": "sea_surface_temp_mean2"}, inplace=True)

# make dataframe of missing values
nan_df = sample_df.isnull().sum(axis=0)

#
# plot_df = sample_df.append(dropped_df)
#
# print(plot_df.head(20))

fig, axes = plt.subplots(3)

sns.regplot(data=dropped_df, x='month', y="sea_surface_temp_drop", ax=axes[0],
            marker='o', color='red', scatter_kws={'s':2})

sns.regplot(data=meanfill_df, x='month', y="sea_surface_temp_mean", ax=axes[1],
            marker='o', color='red', scatter_kws={'s':2})

sns.regplot(data=meanfill2_df, x='month', y="sea_surface_temp_mean2", ax=axes[2],
            marker='o', color='red', scatter_kws={'s':2})

plt.show()