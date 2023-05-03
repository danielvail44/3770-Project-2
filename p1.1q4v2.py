import numpy as np
from matplotlib import pyplot as plt
import data
from scipy.stats import poisson
import math
from scipy.stats import chisquare



bin_width = 3000
interval_range = (0, data.palindromes.max()+bin_width)


hist, bin_edges = np.histogram(data.palindromes, bins=np.arange(*interval_range, bin_width))

oCounts = np.zeros(hist.max() + 1)



for count in hist:
    oCounts[count] += 1
sampleMean = np.mean(oCounts)
sampleVar = np.var(oCounts)

lambda_p = 0
elements = 0
for i, e in enumerate(oCounts):
    lambda_p += i*e
    elements += e
lambda_p = lambda_p/elements

print (lambda_p)
print(elements)


oldCounts = oCounts
oCounts = np.zeros(9)
oCounts = oldCounts[0:9]
oCounts[8] = np.sum(oldCounts[8:14])





print(f"Var: {sampleVar}, mean: {sampleMean}")
print(lambda_p)

eCounts = np.zeros(hist.max() + 1)

poisson_probs = len(hist)*poisson.pmf(np.arange(len(oCounts)), mu=lambda_p)
poisson_probs[-1] += len(hist)*(1-poisson.cdf(8, mu=lambda_p))


print(poisson.stats(lambda_p, moments='mv'))


for i, count in enumerate(oCounts):
    print(f"Plaindrome count: {i}, observed occurrences: {count}, expected: {poisson_probs[i]}")



observed_frequencies = oCounts
expected_frequencies = poisson_probs
print(sum(observed_frequencies))
print(sum(expected_frequencies))
df = len(observed_frequencies-1-1)
print(expected_frequencies)
chi2_statistic, p_value = chisquare(observed_frequencies, expected_frequencies, 9)
print(chi2_statistic)
# Set the significance level
alpha = 0.05
print (p_value)
# Check the null hypothesis of the Poisson distribution
if p_value > alpha:
    print("The null hypothesis of the Poisson distribution is not rejected.")
else:
    print("The null hypothesis of the Poisson distribution is rejected.")

# Compare the estimated Poisson parameter lambda_p with the parameter lambda_e
print(f"Estimated Poisson parameter: lambda_p = {lambda_p:.2f}")

