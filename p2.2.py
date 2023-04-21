import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm


def normalSample():
    return np.random.normal(0,1,25)

baseSample = normalSample()

means = []

for i in range(0,2000):
    sample = np.random.choice(baseSample, 25)
    means.append(np.mean(sample))

plt.hist(means, density=True, bins=40)
x = np.linspace(-1,1,1000)
plt.plot(x, norm(0,1/np.sqrt(25)).pdf(x))
plt.fill_betweenx([0, 2.5], np.percentile(means,2.5), np.percentile(means,97.5), color='g', alpha=0.2)
plt.show()
