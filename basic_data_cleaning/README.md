# Basic Data Cleaning 

## Introduction:
This is an investigation into methods that could be used to fill missing data values in a dataset with time and location data asocciated with the data of interest. The methods tested below are very basic, and are intended to be used as a starting point that can be built upon and tailored to a specific dataset. Four methods were tested: 
 - Baseline
   - Mean temperature value replaces all missing values
 - Chronological
   - Missing value replaced with mean of all previous temperature values
 - Chronological windowed
   - Missing data replaced with mean of previous 30 data values
 - Location 
   - Missing data replaced with mean of 60 adjacent temperature readings 


## Validation data:
This is a collection of experiments with basic data cleaning techniques in Python using the Pandas library. 

The dataset to test the methods was a sample from the NOAA ICOADS 2012 data, and the variable investigated was the sea surface temperature. This dataset was retrieved from [Kaggle](https://www.kaggle.com/datasets/noaa/noaa-icoads) using bigquery to extract the 2012 sea surface temperature only, (the full dataset is huge). As the full dataset for 2012 is very large (approx. 5.5 million rows) a random sample of 10,000 rows was used to minimize computational time while still being a representative sample. The animation below shows the dataset that was used. 

| ![](https://github.com/la-robson/mini_projects/blob/main/basic_data_cleaning/images/sample_data_animation.gif) | 
|:--:| 
| *Animation of 10,000 datapoints randomly sampled from the complete NOAA ICOAADS 2012 sea surface temperature dataset* |
 
To create the testing and validation dataset that was representative of the full dataset the following method was applied:
1. Calculate percentage of missing values in sample dataset (approx. 30%)
2. Drop all missing values to create a ‘complete’ dataset, this is the validation data
3. Create a copy of the validation data and randomly replace values with NaN in the same proportion as the original dataset, this is the test data

The cleaning models could then be applied to the test dataset, and the filled values can be compared to the real values in the validation dataset. In addition to using the MSE score to compare the different methods, the difference between the cleaned data and the validation data was visually checked using KDE plots. These are very similar to histograms they visualize a distribution of data density and are much easier to interpret than scatter plots. 


## Results:
| ![](https://github.com/la-robson/mini_projects/blob/main/basic_data_cleaning/data/clean_comparison_plots/mean_fill.png) | ![](https://github.com/la-robson/mini_projects/blob/main/basic_data_cleaning/data/clean_comparison_plots/chron_mean_fill.png)|
|:--:|:--:| 
| ![](https://github.com/la-robson/mini_projects/blob/main/basic_data_cleaning/data/clean_comparison_plots/chron_mean_window_fill.png) | ![](https://github.com/la-robson/mini_projects/blob/main/basic_data_cleaning/data/clean_comparison_plots/loc_mean_fill.png)|

*KDE contour plot of cleaned data vs validation data for different basic data filling methods*

The table above above shows the KDE plots of each of the models, the ideal would be for the data to all lie on the y=x line, the closest to this is the cleaning method using location based filling prioritizing latitude over longitude. The other plots have a very distinctive y=x line and a horizonal cluster around the mean temperature, this indicates that the data is being filled with values at, or very close to the global mean temperature.


## Conclusions:
From this table it is clear that the location-based filling method was most accurately filling the missing values. This was expected as location is highly influential in the temperature of the ocean. However, the more complex methods do not have a significant improvement over the baseline. There is room for significant improvement in these methods. Firstly the chronological windowed and location method could be optimized by testing different sized sample windows for the mean, the values used here were arbitrarily selected and have not been optimized. Secondly the chronological and location based methods could be combined, so both are taken into account, location is evidently a more important factor, but they both are explanatory variables so should be included. 

Alternative methods that could be considered in future are filling with the mean historical value from the nearest sensor at the previous timestep, or the interpolated values of the nearest three sensors at the previous timestep (triangulation), or the trend over time could be extrapolated forwards to fill the missing value. Clearly it is possible to increase the complexity of the interpolation method, and it would be expected that increasing the complexity would increase the accuracy of the filled in value on average. For the sake of efficiency, it is preferable to use the simplest method that gives an acceptable result. 

