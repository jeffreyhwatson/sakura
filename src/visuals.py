import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def mean_plot(df):
    fig, ax = plt.subplots(figsize=(15,7))
    ax = sns.scatterplot(data=df, x='AD', y='Full-flowering date (DOY)',\
                         color='lightpink', label='Peak Bloom Day')
    ax = sns.lineplot(data=df, x='AD', y='Mean Peak', color='palevioletred',\
                      label='Mean Peak Bloom Day', alpha=.6)
    plt.title('Mean Peak Bloom Day from 864 to 1994', size = 16)
    plt.xlabel(' ', size=16)
    plt.ylabel('Day of Year', size=16)
    plt.legend()
#     plt.savefig('mean_bloom.png', bbox_inches ="tight",\
#                     pad_inches = .25, transparent = False)
    plt.show()

def sakura_plot(df):
    fig, ax = plt.subplots(figsize=(15,7))
    ax = sns.scatterplot(data=df, x='AD', y='Full-flowering date (DOY)',\
                         color='lightpink', label='Peak Bloom Day')
    ax = sns.lineplot(data=df, x='AD', y='5_Year_Ave', color='palevioletred',\
                      label='5-Year Moving Average', alpha=.4)
    plt.title(' 5-Year Moving Average of Peak Bloom Day from 864 to 1994', size = 16)
    plt.xlabel(' ', size=16)
    plt.ylabel('Day of Year', size=16)
    plt.legend()
#     plt.savefig('bloom_year.png', bbox_inches ="tight",\
#                     pad_inches = .25, transparent = False)
    plt.show()
def temp_plot(df):
    fig, ax = plt.subplots(figsize=(15,7))
    ax = sns.lineplot(data=df, x='AD', y='F', color='palevioletred', alpha=.4)
    plt.title('Estimated Mean Temperature for March in Kyoto by Year', size = 16)
    plt.xlabel(' ', size=16)
    plt.ylabel('Degrees Fahrenheit', size=16)
#     plt.savefig('march_temp.png',bbox_inches ="tight",\
#                     pad_inches = .25, transparent = False)
    plt.show()
    
def temp_day_plot(df):
    fig, ax = plt.subplots(figsize=(15,7))
    ax = sns.regplot(data=df, x='F', y='Full-flowering date (DOY)',
                     scatter_kws = {'color': 'lightpink'},\
                     line_kws = {'color': 'palevioletred', 'alpha': 0.4})
    plt.title('Sakura Peak Bloom Day by Temperature', size = 16)
    plt.ylabel('Day of Year', size=16)
    plt.xlabel('Degrees Fahrenheit', size=16)
#     plt.savefig('bloom_temp.png',bbox_inches ="tight",\
#                     pad_inches = .25, transparent = False)
    plt.show()