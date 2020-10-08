import pandas as pd
from matplotlib import pyplot as plt


data = pd.read_csv("countries.csv")

# Compare population growth in the US and China

us = data[data.country == "United States"]

china = data[data.country == "China"]

# Us relative population growth
us_pop = us.population

us_pop_first = us.population.iloc[0]

us_relative_pop_growth = us_pop / us_pop_first * 100

# China relative population growth
china_pop = china.population

china_pop_first = china.population.iloc[0]

china_relative_pop_growth = china_pop / china_pop_first * 100

# Plot relative pop growth

plt.plot(us.year, us_relative_pop_growth)
plt.plot(china.year, china_relative_pop_growth)


plt.legend(["United States", "China"])

plt.xlabel("year")
plt.ylabel("population growth (first-year=100)")


plt.show()
