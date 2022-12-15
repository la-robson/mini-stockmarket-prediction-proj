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
cleaned_data_path = f'../basic_data_cleaning/data/cleaned_data/'
cleaned_files = os.listdir(cleaned_data_path)

print('Cleaned data files in directory: ')
for file in cleaned_files:
    print(file)


# import data
dropped_df = pd.read_csv(''.join([cleaned_data_path, cleaned_files[0]]))

