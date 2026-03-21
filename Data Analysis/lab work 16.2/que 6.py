# 2. Combining and Splitting Arrays
import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])

print("Array 1:", arr1)
print("Array 2:", arr2)

print("Vertical Stack:\n", np.vstack((arr1, arr2)))
print("Horizontal Stack:\n", np.hstack((arr1, arr2)))

#output:-
# Array 1: [1 2 3 4 5]
# Array 2: [10 20 30 40 50]
# Vertical Stack:
#  [[ 1  2  3  4  5]
#  [10 20 30 40 50]]
# Horizontal Stack:
#  [ 1  2  3  4  5 10 20 30 40 50]

