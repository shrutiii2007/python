# 2. Combining and Splitting Arrays

import numpy as np

arr1 = np.array([[1, 2],
              [3, 4]])

arr2 = np.array([[5, 6],
              [7, 8]])

print("Array A:\n", arr1)
print("Array B:\n", arr2)

combined_one = np.concatenate((arr1, arr2),axis=0)
print("Concatenated Array:\n", combined_one)

combined_two = np.concatenate((arr1, arr2),axis=1)
print("Concatenated Array:\n",combined_two)

stack_1 = np.stack((arr1, arr2),axis = 0)
print("stack array:\n",stack_1)

stack_2 = np.stack((arr1, arr2),axis = 2)
print("stack array:\n",stack_2)

hstack = np.hstack((arr1, arr2))
print("hstack:\n",hstack)

#output:-

# Array A:
#  [[1 2]
#  [3 4]]
# Array B:
#  [[5 6]
#  [7 8]]
# Concatenated Array:
#  [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]
# Concatenated Array:
#  [[1 2 5 6]
#  [3 4 7 8]]
# stack array:
#  [[[1 2]
#   [3 4]]

#  [[5 6]
#   [7 8]]]
# stack array:
#  [[[1 5]
#   [2 6]]

#  [[3 7]
#   [4 8]]]
# hstack:
#  [[1 2 5 6]
#  [3 4 7 8]]