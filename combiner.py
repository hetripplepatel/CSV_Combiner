import sys
import csv
import os
import pandas as pd

n = len(sys.argv)

# n is the number of arguments, including this file itself
combined_csv = pd.concat([pd.read_csv(sys.argv[i])
	.assign(filename=os.path.basename(sys.argv[i])) for i in range(1,n)])
# we are concatenating the input csv files. The 0th input is this file itself, so we do not combine it
# .concat concatenates the files
# .assign(filename=...) adds a column called filename with the name 
#of the corresponding file of each row as its entry
print(combined_csv.to_csv(index=False))
# we print the csv but we do not want any index to show up from the different csv files

# The time and space complexities are both linear in the input.
# If we can read each line of the csv files and immediately output it in the combined csv,
# then the space complexity will go down significantly because we will only have one
# row in the memory at a time.

# Instructions to run the file:
# Go to the folder where combiner.py and the csv files are.
# Run "python3 combiner.py inp1.csv inp2.csv ... inpX.csv > output.csv"