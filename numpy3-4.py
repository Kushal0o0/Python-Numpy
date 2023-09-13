import numpy
import numpy as np
from numpy import random

# LMS problems
x = np.array([[1.0,1.0,1.0],[1.0,1.0,1.0],[1.0,1.0,1.0],[1.0,1.0,1.0]])
x = x.reshape(4, 3)
print(np.ones_like(x))

x = np.arange(12)
x = x.reshape(4, 3)
np.ones(x)
########################################################################################################################

# reshaping numpy array
array = numpy.array([1, 2, 3, 4, 5, 6, 7, 8])
print(array, array.shape)

# 2D
reshapedarray2 = array.reshape(4, 2)  # reshapes the array into rows (1st)argument and num of elements in each row (2nd)argument
print(reshapedarray2, reshapedarray2.shape)  # both numbers inplace of arguments has to be multiples of len of elements in original array

# 3D
reshapedarray3 = array.reshape(2, 2, 2)
print(reshapedarray3, reshapedarray3.shape)

# 1D
reshapedarray1 = reshapedarray2.reshape(8, 1)  # reshapes a multiD array into a 1D array with each number inside a list
print(reshapedarray1)
# we can use the (flatten()) function to convert any array into 1D
flattenedarray = reshapedarray2.flatten()
print(flattenedarray)
########################################################################################################################
########################################################################################################################
# accessing numpy array

# slicing
# [start:stop , start:stop]
# [start:stop:step, start:stop:step]

array = numpy.arange(2, 50)
arrayreshaped = array.reshape(6, 8)
print(arrayreshaped)

print(arrayreshaped[1])    # prints out the index number 1 row from the array
print(arrayreshaped[1][0:4])  # ranged slicing

print(arrayreshaped[:, 1])  # prints out the index number 1 column from the array
print(arrayreshaped[0:4, 1])  # ranged slicing

print(arrayreshaped[:, :])  # prints out the entire array
print(arrayreshaped[2:4, 2:4])

print(arrayreshaped[:, :3]) # prints out all the rows of the first three columns
print(arrayreshaped[:, 3:])  # prints out all the rows of except first three columns"""
########################################################################################################################

# integer array indexing

print(arrayreshaped[[0, 1, 2], [1, 2, 3]])  # two separate list to access the array
                                            # 1st list > row number, 2nd list > Nth element from that row"""
########################################################################################################################

# boolean array indexing
ages = numpy.array([10, 32, 42, 35, 31, 25, 58, 26, 33, 34, 39, 50, 40, 38, 30, 27, 60, 29])
big = ages <= 25
big1 = ages > 25
big2 = ages > 40
big3 = ages > 60

print(len(ages[big]), len(ages[big1]), )