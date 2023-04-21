# Parses text file into numpy arrays containing palindrome indexes and relative distances

import numpy as np
from matplotlib import pyplot as plt

text_file = open("CMV_DNA.txt", "r")
lines = text_file.readlines()

palindromes = []

# Parse string list into integer list
for line in lines:
    value = line.strip(" \n")
    if (value != ""):
        palindromes.append(int(value))

# Create list containing distance between consecutive palindromes
distances = []
for i in range(1, len(palindromes)):
    distances.append(palindromes[i]-palindromes[i-1])
distances = np.array(distances)