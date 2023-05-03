import numpy as np
from matplotlib import pyplot as plt
import data
from scipy.stats import nbinom
import math





bin_width = 3000
# Create bin bounds, adding bin_width to the upper bound to ensure all data is included
interval_range = (0, data.palindromes.max()+bin_width)

# Create histogram containing bins generated
hist, bin_edges = np.histogram(data.palindromes, bins=np.arange(*interval_range, bin_width))


oCounts = np.zeros(hist.max() + 1)
# Sort bins into table based on observed number of palindromes per bin
for count in hist:
    oCounts[count] += 1

sampleMean = 0
sampleVar = 0
elements = 0
# Calculate lambda based on expected value of bins
for i, e in enumerate(oCounts):
    sampleMean += i*e
    elements += e
sampleMean = sampleMean/elements

for i, e in enumerate(oCounts):
    sampleVar += (i*e - sampleMean)**2

sampleVar = sampleVar/(elements-1)

#p = sampleMean/sampleVar
#r = (p*sampleMean)/(1-p)
p = 1-sampleMean/sampleVar
r = sampleMean**2/(sampleVar - sampleMean)

print(f"r point estimator: {r}, p point estimator: {p}")
print(f"Var: {sampleVar}, mean: {sampleMean}")


eCounts = np.zeros(hist.max() + 1)

# for i, count in enumerate(eCounts):
#     eCounts[i] = math.comb(i+r-1,i)*p**1*(1-p)**i
#     eCounts[i] = len(hist)*nbinom.pmf(i, r, p)

eCounts = len(hist)*nbinom.pmf(np.arange(len(oCounts)), r, p)



print(nbinom.stats(r, p, moments='mv'))


for i, count in enumerate(oCounts):
    print(f"Plaindrome count: {i}, observed occurrences: {count}, expected: {eCounts[i]}")









# import numpy as np
# from matplotlib import pyplot as plt
# import data
# import scipy.stats as stats



# print (f"Lambda = {lambda_p}")
# print(f"Number of elements: {elements}")

# # Combine bins 8 and up into single bin because expected value <3
# oldCounts = oCounts
# oCounts = np.zeros(9)
# oCounts = oldCounts[0:9]
# oCounts[8] = np.sum(oldCounts[8:14])


# print(f"Var: {sampleVar}, mean: {sampleMean}")

# eCounts = len(hist)*stats.poisson.pmf(np.arange(len(oCounts)), mu=lambda_p)
# eCounts[-1] += len(hist)*(1-stats.poisson.cdf(len(eCounts-1), mu=lambda_p))


# for i, count in enumerate(oCounts):
#     print(f"Plaindrome count: {i}, observed occurrences: {count}, expected: {eCounts[i]:.2f}")



# observed_frequencies = oCounts
# expected_frequencies = eCounts

# test_statistic = 0
# for i in range(0, len(oCounts)):
#     test_statistic += (oCounts[i] - eCounts[i])**2/eCounts[i]

# print(f"\nTest statistic: {test_statistic:.2f}")
# # Number of bins - parameters - 1
# df = len(oCounts) - 2
# alpha = .05
# lBound = stats.chi2.ppf(alpha/2, df)
# uBound = stats.chi2.ppf(1-alpha/2, df)
# print(f"Upper bound: {uBound:.2f}, lower bound: {lBound:.2f}")

# # Check the null hypothesis of the Poisson distribution
# if (test_statistic > uBound) or (test_statistic < lBound):
#     print("The null hypothesis of the Poisson distribution is rejected.")
# else:
#     print("The null hypothesis of the Poisson distribution is not rejected.")

# # Compare the estimated Poisson parameter lambda_p with the parameter lambda_e
# print(f"Estimated Poisson parameter: lambda_p = {lambda_p:.2f}")



