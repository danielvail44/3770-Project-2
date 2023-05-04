import numpy as np
from matplotlib import pyplot as plt
import data

# Set the bin width and the range of the intervals
bin_width = 3000
# Create bin bounds, adding bin_width to the upper bound to ensure all data is included
interval_range = (0, data.palindromes.max()+bin_width)

# Create histogram containing bins generated
hist, bin_edges = np.histogram(data.palindromes, bins=np.arange(*interval_range, bin_width))


oCounts = np.zeros(hist.max() + 1)
# Sort bins into table based on observed number of palindromes per bin
for count in hist:
    oCounts[count] += 1


for i, count in enumerate(oCounts):
    print(f"Plaindrome count: {i}, observed occurrences: {count}")
