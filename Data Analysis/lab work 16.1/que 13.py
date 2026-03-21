# 3. Indexing and Slicing of NumPy Arrays

import numpy as np

arr = np.array([
    [ 1,  2,  3,  4],
    [ 5,  6,  7,  8],
    [ 9, 10, 11, 12],
    [13, 14, 15, 16]
])

result = arr[2:, 2:]

print(result)


#output:-
# [[11 12]
#  [15 16]]

