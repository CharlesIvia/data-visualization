import matplotlib.pyplot as plt
from pandas.io.formats import style
import seaborn as sns
import pandas as pd

df = pd.read_csv("happiness.csv")

print(df.head())

sns.scatterplot(
    x="Economy (GDP per Capita)",
    y="Happiness Score",
    data=df,
    hue="Region",
    size="Freedom",
)

# From this plot, we can conclude that there's a strong positive correlation between
# the economy (GDP per capita) and score of happiness

# Multiple scatter plots

grid = sns.FacetGrid(df, col="Region", hue="Region", col_wrap=5)

grid.map(sns.scatterplot, "Economy (GDP per Capita)", "Health (Life Expectancy)")

grid.add_legend()

# Plotting a 3D scatter plot in seaborn

sns.set(style="darkgrid")

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

x = df["Happiness Score"]
y = df["Economy (GDP per Capita)"]
z = df["Health (Life Expectancy)"]

ax.set_xlabel("Happiness")
ax.set_ylabel("Economy")
ax.set_zlabel("Health")

ax.scatter(x, y, z)

plt.show()
