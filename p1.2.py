import numpy as np
from matplotlib import pyplot as plt
import data

# Load the data
data = np.loadtxt('CMV_DNA.txt', dtype=int)

# Set the bin width and the range of the intervals
bin_width = 3000
interval_range = (1, 229354)

# Compute the histogram of the palindromes
hist, bin_edges = np.histogram(data, bins=np.arange(*interval_range, bin_width))

# Display the table of observed frequencies
print('Interval\tObserved frequency')
for i, count in enumerate(hist):
    interval_start = bin_edges[i]
    interval_end = bin_edges[i+1]
    print(f'[{interval_start}, {interval_end})\t{count}')
