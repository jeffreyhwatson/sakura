# Sakura Bloom Analysis

![sakura](images/sakura.jpeg)

## Background

## Purpose

Descripitve analysis on the Cherry Blossom data set to determine if there are trends in the peak bloom days for Kyoto sakura over time.

## Setup Instructions
To setup the project environment, cd into the project folder and run `conda env create --file sakura.yml` in your terminal. Next, `run conda activate sakura`.

## Data

- Historical Series of Phenological data for Cherry Tree Flowering at Kyoto City (and March Mean Temperature Reconstructions) by Aono and Kazui, 2008; Aono and Saito, 2010; Aono, 2012.

#### Data Understanding

- The the data was presented in the form of two Excel spreadsheets:
    - 'KyotoFullFlower7.xls' (1240 rows of bloom data and information about the primary sources of the the bloom data)
    - 'TempReconst7Final.xls' (1196 rows of temperature data and information about the methodology surrounding the data)

[Data Set Website](http://atmenv.envi.osakafu-u.ac.jp/aono/kyophenotemp4/)

#### Methods & Data Preperation

Python, Pandas, and Seaborn were used for data preparation, analysis and visualization.

Details can be found in the [EDA Notebook](notebooks/eda/sakura_data.ipynb).

- After loading the spreadsheets into two data frames, the keys for each data set were seperated from the raw data and collected into smaller lookup data frames.

- Column names were added to the dataframes, datatype conversions were performed, and null values were dropped. 

- Five-year moving average and fahrenheit temperature features were added and the two data frames were joined.

## Results

We can see that the average peak bloom day has occured around the 105th day of the year through most of the years on record. 

![mean bloom](images/mean_bloom.png)

However, plotting a 5-year moving average reveals that the peak bloom day has been moving earlier in the year over time since the 1800s. 

![bloom year](images/bloom_year.png)

The temperature data also shows a warming trend beginning in the 1800s and continuing into the present.

![march temp](images/march_temp.png)

Lastly, plotting peak bloom against temperature shows a correlation between higher temperatues and earlier peak bloom days.

![bloom temp](images/bloom_temp.png)

## Linear Regression

A simple linear regression model was created with `Full-flowering date (DOY)` as the target and `F` (Mean Temp in Kyoto for March) as the predictor. R-squared and the correlation coefficient for the fahrenheit temperature feature were found and the data and model were checked for adherence to the assumptions of linear reggression.

## Interpretation

Our intercept suggests that if the average March temperature in Kyoto is 0 degrees fahrenhiet, the mean peak bloom day will occur on the 189th day of the year. The fahrenheit (F) coefficient indicates that for every 1 degree rise in mean March temperature, on average the peak bloom day will occur 1.96 days earlier. Lastly, r-squared of .146 says that around 14% of the variance in peak bloom dates can be account for through the mean March temperature in Kyoto.

## Linear Regression Assumptions

The model and data data were found to be mostly in line with the assumptions of linear regression. The only assumption broken was the homoscadasticity of the residuals.

## Conclusion

The data do indicate that the peak bloom day has been occuring earlier in the year over time and that this is correlated with a rise in mean temperatures for March in Kyoto. Our simple model suggests that for every 1 degree fahreheit rise in mean temperature for March, the peak bloom day will occur 1.96 days earlier on average. We also find that mean March temperature accounts for about 15% of the variance in peak bloom day.

## Repo Structure
```
├── data
│   ├── KyotoFullFlower7.xls
│   └── TempReconst7Final.xls
├── images
│   ├── bloom_temp.png
│   ├── bloom_year.png
│   ├── march_temp.png
│   ├── mean_bloom.png
│   └── sakura.jpeg
├── notebooks
│   ├── eda
│   │   └── sakura_data.ipynb
│   └── report
├── sakura.md
├── sakura.yml
└── src
    └── visuals.py

```