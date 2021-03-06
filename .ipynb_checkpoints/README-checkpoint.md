# Sakura Bloom Analysis

A small side-project undertaken for practice and personal enjoyment.

![sakura](images/Cherry_Blossom.jpeg)

## Background

Cherry blossom viewing (known as hanami in Japanese) has been an important part of Japanese culture for thousands of years, and it has been chronicled in poems, literature, and official documents since at least the 800s. Because of this long historical record we can track the date of the peak bloom day of the sakura (cherry blossom trees) and how it has changed over time.

## Purpose

Descriptive analysis on the Cherry Blossom data set to determine if there are trends in the peak bloom days for Kyoto sakura over time. If trends are found, simple modeling will be employed to further investigate the data.

## Repo Structure
```
.
├── README.md
├── data
├── images
├── notebooks
│   └── eda
├── sakura.yml
└── src
```

## Setup Instructions
To setup the project environment, cd into the project folder and run `conda env create --file sakura.yml` in your terminal. Next, run `conda activate sakura`.

## Data

- Historical Series of Phenological data for Cherry Tree Flowering at Kyoto City (and March Mean Temperature Reconstructions) by Aono and Kazui, 2008; Aono and Saito, 2010; Aono, 2012.

#### Data Understanding

- The the data was presented in the form of two Excel spreadsheets:
    - 'KyotoFullFlower7.xls' (1240 rows of bloom data and information about the primary sources of the the bloom data)
    - 'TempReconst7Final.xls' (1196 rows of temperature data and information about the methodology surrounding the data)

[Data Set Website](http://atmenv.envi.osakafu-u.ac.jp/aono/kyophenotemp4/)

#### Methods & Data Preperation

Python, Pandas, Statsmodels, and Seaborn were used for data preparation, analysis and visualization.

Details can be found in the [EDA Notebook](notebooks/eda/sakura_eda.ipynb).

- After loading the spreadsheets into two data frames, the keys for each data set were separated from the raw data and collected into smaller lookup data frames.

- Column names were added to the data frames, datatype conversions were performed, and null values were dropped. 

- Five-year moving average for peak bloom day, mean peak bloom day, and fahrenheit temperature features were added and the two data frames were joined.

## Results

We can see that the average peak bloom day has occured around the 105th day of the year through most of the years on record. 

![mean bloom](images/mean_bloom.png)

However, plotting a 5-year moving average reveals that the peak bloom day has been moving earlier in the year over time since the 1800s. 

![bloom year](images/bloom_year.png)

The temperature data also shows a warming trend beginning in the 1800s and continuing into the present.

![march temp](images/march_temp.png)

Lastly, plotting peak bloom against temperature shows a correlation between higher temperatures and earlier peak bloom days.

![bloom temp](images/bloom_temp.png)

## Linear Regression

A simple linear regression model was created with `Full-flowering date (DOY)` as the target and `F` (Mean Temp in Kyoto for March) as the predictor. R-squared and the correlation coefficient for the fahrenheit temperature feature were found and the data and model were checked for adherence to the assumptions of linear regression.

## R-Squared

***R<sup>2</sup> = .146***

## Regression Formula

***D = 189.14 -1.97T***

Where D is the Peak Bloom Day and T is the average temperature for March in Kyoto for the year.

## Interpretation

Our intercept suggests that for an average March temperature in Kyoto of 0 degrees fahrenheit, the mean peak bloom day will occur on the 189th day of the year. The fahrenheit (F) coefficient indicates that for every 1 degree rise in mean March temperature, the peak bloom day will occur 1.97 days earlier on average. Lastly, the model's R-squared value of .146 says that around 15% of the variance in peak bloom dates can be accounted for through the mean March temperature in Kyoto.

## Linear Regression Assumptions

The model and data were found to adhere to most of the assumptions of linear regression. The only assumption broken was homoscedasticity of the residuals.

![residuals](images/residuals.png)

## Conclusion

The data do indicate that the peak bloom day has been occurring earlier in the year over time and that this is correlated with a rise in mean temperatures for March in Kyoto. Our simple model suggests that for every 1 degree fahrenheit rise in mean temperature for March, the peak bloom day will occur 1.96 days earlier on average. We also find that mean March temperature accounts for about 15% of the variance in peak bloom day.
