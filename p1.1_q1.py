import numpy as np
from matplotlib import pyplot as plt
import data


plt.hist(data.distances, density=True, bins=15)


print(f"Average distance between palindromes: {round(np.mean(data.distances),2)}")

# Exponential PDF function
def e(x, l):
    return l*np.exp(-l*x)
x = np.linspace(0,data.distances.max(),data.distances.max())

# Lambda chosen as 1/mean(distance) because the mean of an exponential distribution is 1/lamda
plt.plot(x, e(x,1/np.mean(data.distances)), color='red')
plt.show()

