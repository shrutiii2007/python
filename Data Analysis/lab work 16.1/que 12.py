# 3. Indexing and Slicing of NumPy Arrays

import numpy as np

arr = np.arange(1, 10)
print(arr)
print()
matrix = arr.reshape(3, 3)
print("Matrix:\n", matrix)

element = matrix[1, 2]  
print("element at the second row and third column:-",element)

# output:-
# [1 2 3 4 5 6 7 8 9]
# Matrix:
#  [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
# element at the second row and third column:- 6



