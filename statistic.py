# Python code to demonstrate the working of
# variance() function of Statistics Module

# Importing Statistics module
import statistics
import numpy as np
import pandas as pd

from pandas import Series, DataFrame

series_obj = Series(np.arange(5), index=[
                    'lp 1', 'lp 2', 'lp 3', 'lp 4', 'lp 5', ])
print(series_obj)
# select by index
series_obj['lp 3']
# select 0 and 5 object
series_obj[[0, 3]]
series_obj['lp 2':'lp 4']
np.random.seed(25)
# create data frame object and reshape to 6x6 matrix
DataFrame_obj = DataFrame(np.random.rand(36).reshape((6, 6)), index=[
                          'a', 'b', 'c', 'd', 'e', 'f'], columns=['A', 'B', 'C', 'D', 'E', 'F'])
print(DataFrame_obj)
# Creating a sample of data
sample = [2.74, 1.23, 2.63, 2.22, 3, 1.98]
file = open("ng_test.txt", "w+", encoding='utf-8')
# Prints variance of the sample set

# Function will automatically calculate
# it's mean and set it as xbar
print("Variance of sample set is % s"
      % (statistics.variance(sample)))
# for x in range(1, 11)
# file.write(", ".join(str(e) for e in sample))
