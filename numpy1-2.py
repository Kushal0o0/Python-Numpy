import numpy as np
from numpy import random

# LMS problems
a = np.array([[1, 2, 3], [0, 1, 4]])
b = np.zeros((2, 3), dtype=np.int16)
c = np.ones((2, 3), dtype=np.int16)
d = a + b + c
print(d)
print(d[1, 2])
#################################################################################################################

# converting a list into np array
list = [1, 2, 3, 4, 5]
nlist = np.array(list)
print(nlist)
print(nlist + 1)  # adds +1 to each element of the array
#################################################################################################################

# one dimensional array
l = [1, 2, 3, 4, 5, 6]
oned_l = np.array(l)
print(f"{oned_l}, {type(oned_l)}, {oned_l.ndim} dimension")

# multi dimensional array (2d)
l2 = [[1, 2], [3, 4]]
twod_l2 = np.array(l2)
print(f"{twod_l2}, {type(twod_l2)} , {twod_l2.ndim} dimension")

# multi dimensional array (3d)
l3 = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[13, 14, 15], [16, 17, 18]]]
threed_l3 = np.array(l3)
print(f"{threed_l3}, {type(threed_l3)}, {threed_l3.ndim} dimension")
#################################################################################################################

# random function inside the numpy library
x = random.randint(100, size=5)  # generates 1d array containing 5 random integers from 1 to 100
print(f"x = {x}")

y = random.randint(100, size=(
3, 5))  # generates 2d array containing 3 rows and each rows contains 5 random integers from 1 to 100
print(f"y = {y}\n")
#################################################################################################################

# creating numpy array using aarange
array = np.arange(5,
                  dtype=float)  # generates an array from 0 to (N-1) number, dtype = datatype can either be int or float or object
print(f"array0 {array}")  # if dtype is not specified the default will be int

array1 = np.arange(5, 10)  # generates an array from Nth number to (N-1) number
print(f"array1 {array1}")

array2 = np.arange(2, 20, 2)  # generates and array from Nth number to (N-1) number with a jump(3rd argument)
print(f"array2 {array2}")
#################################################################################################################

# zeros and ones
# the zeros and ones create new arrays of specified dimensions filled with  0s and 1s
array = np.zeros(4,
                 dtype=int)  # generates and array with N number of zeros dtype = float, int or object default will be float
print(f" array {array}")

array1 = np.ones([4, 3], int)  # generates a multidimensional array argument 1(0) = rows, 1(1) = elements in each row
print(f" array1 {array1}")

array2 = np.ones(10) * 5
print(array2)
#################################################################################################################

# linspace
# return evenly spaced numbers over a specified interval

array = np.linspace(1, 10, num=25)  # argument 3 default will be 50
print(array)
