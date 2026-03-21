# 1. Mathematical Operations
import numpy as np
arr = np.array([1, 2, 3, 4, 5])

mean = arr.mean()  # ye mean dega
std = arr.std()    # ye std dev dega

normal_arr = (arr - mean) / std
# Element ko mean se minus karke std se divide karo → normalized array milega.

print("Original array:", arr)
print("Normalized array:", normal_arr)

#output:-
# Original array: [1 2 3 4 5]
# Normalized array: [-1.41421356 -0.70710678  0.          0.70710678  1.41421356]
