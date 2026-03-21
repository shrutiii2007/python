# 3. Search, Sort, Aggregating/Statistical Functions

import numpy as np

arr = np.array([
    [3, 1, 2],
    [9, 5, 6],
    [7, 4, 8]
])

print("Original Array:")
print(arr)

# Original Array:
# [[3 1 2]
#  [9 5 6]
#  [7 4 8]]


row_sorted = np.sort(arr, axis=1)

print("\nRow-wise Sorted Array:")
print(row_sorted)

# Row-wise Sorted Array:
# [[1 2 3]
#  [5 6 9]
#  [4 7 8]]

col_sorted = np.sort(arr, axis=0)

print("\nColumn-wise Sorted Array:")
print(col_sorted)

# Column-wise Sorted Array:
# [[3 1 2]
#  [7 4 6]
#  [9 5 8]]

flat_sorted = np.sort(arr, axis=None)

print("\nCompletely Sorted Array:")
print(flat_sorted)

# Completely Sorted Array:
# [1 2 3 4 5 6 7 8 9]


