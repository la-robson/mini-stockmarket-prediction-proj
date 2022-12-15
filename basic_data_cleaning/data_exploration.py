# import libraries
import pandas as pd
pd.options.display.float_format = '{:,.2f}'.format
import matplotlib.pyplot as plt
import seaborn as sns

print('Libraries imported.')

# define variables
sample_data_path = '../basic_data_cleaning/data/original_data/noaa_icoads_2012_sample.csv'
plot_save_path = f'../basic_data_cleaning/data/data_exploration/'
n = 5000    # sample size

# import data
sample_df = pd.read_csv(sample_data_path)

# explore the data:

# summarise data
# make dataframe of missing values
nan_df = sample_df.isnull().sum(axis=0)

# overview
print('\nOverview of dataset:')
print(sample_df.describe())
# display number of and proportion of missing values
print('Number of missing values:\n', nan_df)
perc_nan_df  = 100*nan_df/len(sample_df)
print('\n\nPercent of missing values:\n', perc_nan_df)

# visualise distribution
my_pairplot = sns.pairplot(sample_df.sample(5000).drop('id', axis=1),
                           corner=False,
                           plot_kws=dict(marker=".", s=6))
my_pairplot.map_lower(sns.kdeplot, levels=6, color="black")
my_pairplot.fig.suptitle(f'Distribution of {n} point random sample of NOAA ICOADS 2012 dataset', y=1.1)
my_pairplot.savefig(''.join([plot_save_path, 'distribution_pairplot.png']))
print('\nPlot saved at: ', plot_save_path)
plt.show()
