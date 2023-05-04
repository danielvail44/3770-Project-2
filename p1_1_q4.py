import numpy as np
from matplotlib import pyplot as plt
import data
import scipy.stats as stats



bin_width = 3000
# Create bin bounds, adding bin_width to the upper bound to ensure all data is included
interval_range = (0, data.palindromes.max()+bin_width)

# Create histogram containing bins generated
hist, bin_edges = np.histogram(data.palindromes, bins=np.arange(*interval_range, bin_width))


oCounts = np.zeros(hist.max() + 1)
# Sort bins into table based on observed number of palindromes per bin
for count in hist:
    oCounts[count] += 1
sampleMean = np.mean(oCounts)
sampleVar = np.var(oCounts)

lambda_p = 0
elements = 0
# Calculate lambda based on expected value of bins
lambda_p = np.mean(hist)

print (f"Lambda = {lambda_p}")
print(f"Number of elements: {elements}")

# Combine bins 8 and up into single bin because expected value <3
oldCounts = oCounts
oCounts = np.zeros(9)
oCounts = oldCounts[0:9]
oCounts[8] = np.sum(oldCounts[8:14])


print(f"Var: {sampleVar}, mean: {sampleMean}")

eCounts = len(hist)*stats.poisson.pmf(np.arange(len(oCounts)), mu=lambda_p)
eCounts[-1] += len(hist)*(1-stats.poisson.cdf(len(eCounts-1), mu=lambda_p))


for i, count in enumerate(oCounts):
    print(f"Plaindrome count: {i}, observed occurrences: {count}, expected: {eCounts[i]:.2f}")



observed_frequencies = oCounts
expected_frequencies = eCounts

test_statistic = 0
for i in range(0, len(oCounts)):
    test_statistic += (oCounts[i] - eCounts[i])**2/eCounts[i]

print(f"\nTest statistic: {test_statistic:.2f}")
# Number of bins - parameters - 1
df = len(oCounts) - 2
alpha = .05
lBound = stats.chi2.ppf(alpha/2, df)
uBound = stats.chi2.ppf(1-alpha/2, df)
print(f"Upper bound: {uBound:.2f}, lower bound: {lBound:.2f}")

# Check the null hypothesis of the Poisson distribution
if (test_statistic > uBound) or (test_statistic < lBound):
    print("The null hypothesis of the Poisson distribution is rejected.")
else:
    print("The null hypothesis of the Poisson distribution is not rejected.")

# Compare the estimated Poisson parameter lambda_p with the parameter lambda_e
print(f"Estimated Poisson parameter: lambda_p = {lambda_p:.2f}")

