import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10, 11,12])
print(arr)

reshaped_arr = arr.reshape(4,3)
print(reshaped_arr)

flattened_arr = reshaped_arr.flatten()
flattened_arr[0] = 20
print(flattened_arr)
print(reshaped_arr) # original array remains unchanged

raveled_arr = reshaped_arr.ravel()
raveled_arr[0] = 30
print(raveled_arr)
print(reshaped_arr) # original array is changed