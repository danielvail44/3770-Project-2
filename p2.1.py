import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm
import math

def normalSample():
    return np.random.normal(0,1,20)

sampleMeans = []

for i in range(0,2000):
    sample = normalSample()
    sampleMeans.append(np.mean(sample))

plt.hist(sampleMeans, density=True, bins=40)
x = np.linspace(-1,1,1000)
plt.plot(x, norm(0,1/np.sqrt(20)).pdf(x))


plt.show()

print(f"Theoretical mean: 0, Theoretical standard error: {round(1/np.sqrt(20),2)}")
print(f"Simulated mean: {np.mean(sampleMeans)}, simulated standard error: {round(np.std(sampleMeans),2)}")

plt.hist(sampleMeans, density=True, bins=40)
plt.fill_betweenx([0, 2], np.percentile(sampleMeans,5), np.percentile(sampleMeans,95), color='g', alpha=0.2)  # Mark between 0 and the highest bar in the histogram
plt.show()

