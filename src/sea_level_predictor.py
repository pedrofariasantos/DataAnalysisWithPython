import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')
    fig, ax = plt.subplots()
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    result = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = np.arange(df['Year'].min(), 2051)
    sea_level_predicted = result.slope * years_extended + result.intercept
    ax.plot(years_extended, sea_level_predicted, 'r')
    df_recent = df[df['Year'] >= 2000]
    result_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = np.arange(2000, 2051)
    sea_level_recent_predicted = result_recent.slope * years_recent + result_recent.intercept
    ax.plot(years_recent, sea_level_recent_predicted, 'g')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    plt.savefig('sea_level_plot.png')
    return plt.gca().figure
