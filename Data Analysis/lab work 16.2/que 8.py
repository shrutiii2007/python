# 2. Combining and Splitting Arrays
import numpy as np
arr = np.array([[ 1,  2,  3,  4],
                [ 5,  6,  7,  8],
                [ 9, 10, 11, 12],
                [13, 14, 15, 16]])

print("Original array:")
print(arr)

top, bottom = np.vsplit(arr, 2)
top_left, top_right = np.hsplit(top, 2)
bottom_left, bottom_right = np.hsplit(bottom, 2)

print("Top-left:\n", top_left)
print("Top-right:\n", top_right)
print("Bottom-left:\n", bottom_left)
print("Bottom-right:\n", bottom_right)

#output:-
# Original array:
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]
#  [13 14 15 16]]
# Top-left:
#  [[1 2]
#  [5 6]]
# Top-right:
#  [[3 4]
#  [7 8]]
# Bottom-left:
#  [[ 9 10]
#  [13 14]]
# Bottom-right:
#  [[11 12]
#  [15 16]]

