import pandas as pd
from matplotlib import pyplot as plt


# Load data from csv

sample_data = pd.read_csv("sample_data.csv")
print(sample_data)

print(type(sample_data))

col_a = sample_data.column_a
col_b = sample_data.column_b
col_c = sample_data.column_c

print(col_a)
print(col_b)
print(col_c)
print(type(col_a))

first = sample_data.column_c.iloc[0]
print(first)

plt.xlabel("Column a")
plt.ylabel("Column b and c")

plt.plot(sample_data.column_a, sample_data.column_b)
plt.plot(sample_data.column_a, sample_data.column_c, "o")

plt.show()
