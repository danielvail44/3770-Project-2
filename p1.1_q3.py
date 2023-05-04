import numpy as np
from matplotlib import pyplot as plt
import data

# Load the data
data = np.loadtxt('CMV_DNA.txt', dtype=int)

# Set the bin width and the range of the intervals
bin_width = 3000
interval_range = (0, data.max()+bin_width)

# Compute the histogram of the palindromes
hist, bin_edges = np.histogram(data, bins=np.arange(*interval_range, bin_width))

# Estimate λp using the method of moment estimation
lamda_mom = np.mean(hist)
# Estimate λp using the maximum likelihood estimation
lamda_mle = np.sum(hist) / len(hist)

# Display the estimates
print(f"Method of moment estimation: λp = {lamda_mom:.2f}")
print(f"Maximum likelihood estimation: λp = {lamda_mle:.2f}")
