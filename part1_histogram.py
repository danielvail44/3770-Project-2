import numpy as np
from matplotlib import pyplot as plt
import scipy.special
import scipy

text_file = open("CMV_DNA.txt", "r")
lines = text_file.readlines()

palindromes = []

# Parse string list into integer list
for line in lines:
    value = line.strip(" \n")
    if (value != ""):
        palindromes.append(int(value))

# Create list containing distance between consecutive palindromes
distances = []
for i in range(1, len(palindromes)):
    distances.append(palindromes[i]-palindromes[i-1])
distances = np.array(distances)


plt.hist(distances, density=True, bins=15)


print(f"Average distance between palindromes: {round(np.mean(distances),2)}")

# Exponential PDF function
def e(x, l):
    return l*np.exp(-l*x)
x = np.linspace(0,5000,5000)

# Lambda chosen as 1/mean(distance) because the mean of an exponential distribution is 1/l
plt.plot(x, e(x,1/np.mean(distances)), color='red')
plt.show()

