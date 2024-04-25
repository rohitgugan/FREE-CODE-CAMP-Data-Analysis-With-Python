import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Import the data using Pandas
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")

# Task 2: Clean the data
# Filter out days when page views were in the top or bottom 2.5% of the dataset
df = df[
    (df["value"] >= df["value"].quantile(0.025)) &
    (df["value"] <= df["value"].quantile(0.975))
]

# Task 3: Create a draw_line_plot function
def draw_line_plot():
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.plot(df.index, df["value"], color="r", linewidth=1)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    plt.show()

# Task 4: Create a draw_bar_plot function
def draw_bar_plot():
    df_bar = df.copy()
    df_bar["month"] = df_bar.index.month_name()
    df_bar["year"] = df_bar.index.year

    df_bar = df_bar.groupby(["year", "month"]).mean().unstack()

    fig, ax = plt.subplots(figsize=(14, 7))
    df_bar.plot(kind="bar", ax=ax)
    ax.set_title("Average Page Views Per Year and Month")
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.legend(title="Months", labels=range(1, 13), title_fontsize="15")
    plt.show()

# Task 5: Create a draw_box_plot function
def draw_box_plot():
    df_box = df.copy()
    df_box["year"] = df_box.index.year
    df_box["month"] = df_box.index.strftime("%b")

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 8))

    sns.boxplot(x="year", y="value", data=df_box, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    sns.boxplot(x="month", y="value", data=df_box, ax=axes[1], order=[
                'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    plt.show()

# Call the functions
draw_line_plot()
draw_bar_plot()
draw_box_plot()
