# 1. Mathematical Operations

import numpy as np
arr1 = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

arr2 = np.array([[9, 2, 17],
                   [61, 35, 4],
                   [34, 22, 11]])

print("addition:-",arr1 + arr2)
print("Subtraction:", arr1 - arr2) 
print("Multiplication:", arr1 * arr2)
print("Division:", arr1 / arr2)


# 1. Create two NumPy arrays of shape (3, 3) and 
# perform element-wise addition, subtraction, 
# multiplication, and division.

#output:-
# addition:- [[10  4 20]
#  [65 40 10]
#  [41 30 20]]
# Subtraction: [[ -8   0 -14]
#  [-57 -30   2]
#  [-27 -14  -2]]
# Multiplication: [[  9   4  51]
#  [244 175  24]
#  [238 176  99]]
# Division: [[0.11111111 1.         0.17647059]
#  [0.06557377 0.14285714 1.5       ]
#  [0.20588235 0.36363636 0.81818182]]

