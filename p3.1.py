import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm
import p1_1_q4




baseSample = p1_1_q4.hist
l = np.mean(baseSample)

means = []

for i in range(0,2000):
    sample = np.random.poisson(l)
    means.append(np.mean(sample))
means = np.array(means)

bootstrapMean = np.mean(means)

diffs = means - np.full(means.shape, bootstrapMean)
diffs = np.sort(diffs)

plt.hist(means, density=True, bins=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])
plt.fill_betweenx([0, .25], bootstrapMean + diffs[int(diffs.size*.025)], bootstrapMean + diffs[int(diffs.size*.975)] , color='g', alpha=0.2)  # Mark between 0 and the highest bar in the histogram
print(diffs[int(diffs.size*.025)])
print(diffs[int(diffs.size*.975)])
plt.show()