import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("happiness.csv")

print(df.head())

sns.scatterplot("Economy (GDP per Capita)", "Happiness Score", data=df)

# From this plot, we can conclude that there's a strong positive correlation between
# the economy (GDP per capita) and score of happiness

# Multiple scatter plots

grid = sns.FacetGrid(df, col="Region", hue="Region", col_wrap=5)

grid.map(sns.scatterplot, "Economy (GDP per Capita)", "Health (Life Expectancy)")

grid.add_legend()
plt.show()
