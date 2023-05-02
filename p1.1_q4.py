import numpy as np
from scipy.stats import poisson, chi2, chisquare, chi2_contingency

# Load the data
data = np.loadtxt('CMV_DNA.txt', dtype=int)

# Set the bin width and the range of the intervals
bin_width = 3000
interval_range = (0, 229354+3000)

# Compute the histogram of the palindromes
hist, bin_edges = np.histogram(data, bins=np.arange(*interval_range, bin_width))

# Compute the expected frequencies under the Poisson distribution with parameter lambda_p
lambda_p = np.mean(hist)
poisson_probs = poisson.pmf(np.arange(len(hist)), mu=lambda_p) * 296

# Compute the expected frequencies under the exponential distribution with parameter lambda_e
lambda_e = 1 / lambda_p
exponential_probs = poisson_probs * np.exp(-lambda_e) * lambda_e

# Compute the chi-squared statistic and the p-value
observed_frequencies = hist
expected_frequencies = poisson_probs
print(sum(observed_frequencies))
print(sum(expected_frequencies))
df = len(hist) - 1
chi2_statistic, p_value = chisquare(observed_frequencies, expected_frequencies, df)

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
print(f"Parameter of the exponential distribution: lambda_e = {lambda_e:.2f}")
