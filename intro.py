import pandas as pd
from matplotlib import pyplot as plt

x = [1, 2, 3]
y = [1, 4, 9]
z = [10, 5, 0]

# Plot lines

plt.plot(x, y)
plt.plot(x, z)

# Labels
plt.title("Test plot")
plt.xlabel("X")
plt.ylabel("Y and Z")

# Legend

plt.legend(["This is Y", "This is Z"])

plt.show()
