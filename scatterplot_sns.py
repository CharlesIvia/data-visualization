import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns

# CREATE DATA

# Create an empty dataframe

df = pd.DataFrame()

# Add columns

df["x"] = random.sample(range(1, 1000), 5)
df["y"] = random.sample(range(1, 1000), 5)
df["z"] = [1, 0, 0, 1, 0]
df["k"] = ["male", "male", "male", "female", "female"]

# View first few rows of data

print(df.head())

# SCATTERPLOT

# Set style of scatterplot

sns.set_context("notebook", font_scale=1.1)
sns.set_style("ticks")

# Create scatterplot of dataframe

sns.lmplot(
    "x",  # Horizontal axis
    "y",  # Vertical axis
    data=df,  # Data source
    fit_reg=False,  # Don't fit a regression line
    hue="z",  # Set color
    scatter_kws={"marker": "D", "s": 100},  # Set marker styke
)  # Set marker size

# Set title

plt.title("Histogram of IQ")

# Set x-axis label
plt.xlabel("Time")

# Set y-axis label
plt.ylabel("Deaths")

plt.show()
