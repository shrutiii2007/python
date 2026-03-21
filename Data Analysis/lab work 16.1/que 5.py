# 1. Introduction to NumPy
import numpy as np

list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]

numpy_array1 = np.array([1, 2, 3, 4, 5])
numpy_array2 = np.array([5, 4, 3, 2, 1])

list_result = [x + y for x, y in zip(list1, list2)]
# pairs num: (1, 5), (2, 4), (3, 3), and so on.
# 1 + 5 = 6, 2 + 4 = 6, etc.new list: [6, 6, 6, 6, 6].
numpy_result = numpy_array1 + numpy_array2       # same thing will happen 

print("List result:", list_result)
print("NumPy result:", numpy_result)

# output:-
# List result: [6, 6, 6, 6, 6]
# NumPy result: [6 6 6 6 6]
