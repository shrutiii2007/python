# 2. Combining and Splitting Arrays
import numpy as np

arr3D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("original Array:\n",arr3D)

flattened = arr3D.flatten()
print("flattened Array:\n",flattened)

reshape = arr3D.reshape(2,2,2)
print("reshaped Array:\n",reshape)

#output:-
# original Array:
#  [[[1 2]
#   [3 4]]

#  [[5 6]
#   [7 8]]]
# flattened Array:
#  [1 2 3 4 5 6 7 8]
# reshaped Array:
#  [[[1 2]
#   [3 4]]

#  [[5 6]
#   [7 8]]]