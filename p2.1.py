import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm
import math

# Generate an array with 25 normally distributed random values
def normalSample():
    return np.random.normal(0,1,25)

sampleMeans = []

# Generate 2000 random arrays
for i in range(0,2000):
    sample = normalSample()
    sampleMeans.append(np.mean(sample))

# Plot histogram, normal PDF
plt.hist(sampleMeans, density=True, bins=40)
x = np.linspace(-1,1,1000)
plt.plot(x, norm(0,1/np.sqrt(25)).pdf(x))
plt.show()


print(f"Theoretical mean: 0, Theoretical standard error: {round(1/np.sqrt(20),2)}")
print(f"Simulated mean: {np.mean(sampleMeans)}, simulated standard error: {round(np.std(sampleMeans),2)}")

# Plot histogram with confidence interval
plt.hist(sampleMeans, density=True, bins=40)
plt.fill_betweenx([0, 2.5], np.percentile(sampleMeans,2.5), np.percentile(sampleMeans,97.5), color='g', alpha=0.2) 
plt.show()

