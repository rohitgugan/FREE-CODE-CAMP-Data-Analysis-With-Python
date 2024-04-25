import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv", sep = ",")
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]

    # Create scatter plot
    fig , ax = plt.subplots()
    plt.scatter(x,y)

    # Create first line of best fit
    res = linregress(x,y)
    xpredic1 = pd.Series(i for i in range(1800,2050))
    ypredic1 = res.slope * xpredic1 + res.intercept
    plt.plot(xpredic1, ypredic1, "r")

    # Create second line of best fit
    df2 = df[df["Year"] >= 2000]
    x1 = df2["Year"]
    y1 = df2["CSIRO Adjusted Sea Level"]
    res = linregress(x1, y1)
    xpredic2 = pd.Series(i for i in range(2000,2050))
    ypredic2 = res.slope * xpredic2 + res.intercept
    plt.plot(xpredic2, ypredic2, "blue")

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")


    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
