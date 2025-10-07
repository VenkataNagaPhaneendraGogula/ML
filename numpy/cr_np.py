import numpy as np

# 1D array
np_arr = np.array([1, 2, 3])
print(np_arr)
print(np_arr.dtype) # Type of array
print(np_arr.shape) # Shape of array
print(np_arr.size)  # Size of array
print(np_arr.ndim) # Number of dimensions

# 2D array
np_arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np_arr_2d)
print(np_arr.dtype) # Type of array
print(np_arr.shape) # Shape of array
print(np_arr.size)  # Size of array
print(np_arr.ndim) # Number of dimensions

zeros = np.zeros((3, 4), dtype=int) # to create zeros array
print(zeros)

ones = np.ones((2, 3), dtype=int) # to create ones array
print(ones)

arr_r = np.arange(1,11) # to arrange values in array
print(arr_r)

arr_r2 = np.linspace(1, 10, 5, dtype=int) # to define values in array with specific number of elements
print(arr_r2)