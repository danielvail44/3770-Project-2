import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm


def normalSample():
    return np.random.normal(0,1,25)

baseSample = normalSample()
baseMean = np.mean(baseSample)
baseSD = np.std(baseSample)

means = []

for i in range(0,2000):
    sample = np.random.normal(baseMean, baseSD, 25)
    means.append(np.mean(sample))
means = np.array(means)

bootstrapMean = np.mean(means)

diffs = means - np.full(means.shape, bootstrapMean)
diffs = np.sort(diffs)

x = np.linspace(-1,1,1000)
plt.hist(means, density=True, bins=40)
plt.plot(x, norm(0,1/np.sqrt(25)).pdf(x))
plt.fill_betweenx([0, 2.5], bootstrapMean + diffs[int(diffs.size*.025)], bootstrapMean + diffs[int(diffs.size*.975)] , color='g', alpha=0.2)  # Mark between 0 and the highest bar in the histogram
print(diffs[int(diffs.size*.025)])
print(diffs[int(diffs.size*.975)])
plt.show()