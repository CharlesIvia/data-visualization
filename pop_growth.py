import pandas as pd
from matplotlib import pyplot as plt


data = pd.read_csv("countries.csv")
print(data)

#Compare population growth in the US and China

us = data[data.country == "United States"]

china = data[data.country == "China"]
print(us)
print(china)


#Plot US and China population growth

plt.plot(us.year, us.population / 10**6)
plt.plot(china.year, china.population / 10**6)


plt.legend(["United States", "China"])

plt.xlabel("year")
plt.ylabel("population")

plt.show()