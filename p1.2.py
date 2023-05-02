import numpy as np
from matplotlib import pyplot as plt
import data
from scipy.stats import nbinom
import math

sampleMean = np.mean(data.distances)
sampleVar = np.var(data.distances)

p = sampleMean/sampleVar
r = (p*sampleMean)/(1-p)

print(f"r point estimator: {r}, p point estimator: {p.round(8)}")
print(f"Var: {sampleVar}, mean: {sampleMean}")
bin_width = 3000
interval_range = (0, data.palindromes.max()+bin_width)


hist, bin_edges = np.histogram(data.palindromes, bins=np.arange(*interval_range, bin_width))

oCounts = np.zeros(hist.max() + 1)

for count in hist:
    oCounts[count] += 1

eCounts = np.zeros(hist.max() + 1)

for i, count in enumerate(eCounts):
    #eCounts[i] = math.comb(i+1-1,i)*p**1*(1-p)**i*3000
    eCounts[i] = nbinom.pmf(3000, r*(i+1), p)

print(nbinom.stats(r, p, moments='mv'))


for i, count in enumerate(oCounts):
    print(f"Plaindrome count: {i}, observed occurrences: {count}, expected: {eCounts[i]}")

fig, ax = plt.subplots(1, 1)
x = np.arange(nbinom.ppf(0.01, r, p),
              nbinom.ppf(0.99, r, p))
ax.plot(x, nbinom.pmf(x, r, p), 'bo', ms=8, label='nbinom pmf')
ax.vlines(x, 0, nbinom.pmf(x, r, p), colors='b', lw=5, alpha=0.5)
n=r
mean, var, skew, kurt = nbinom.stats(n, p, moments='mvsk')
x = np.arange(nbinom.ppf(0.01, n, p),
              nbinom.ppf(0.99, n, p))
ax.plot(x, nbinom.pmf(x, n, p), 'bo', ms=8, label='nbinom pmf')
ax.vlines(x, 0, nbinom.pmf(x, n, p), colors='b', lw=5, alpha=0.5)
rv = nbinom(n, p)
ax.vlines(x, 0, rv.pmf(x), colors='k', linestyles='-', lw=1,
        label='frozen pmf')
ax.legend(loc='best', frameon=False)
plt.show()


