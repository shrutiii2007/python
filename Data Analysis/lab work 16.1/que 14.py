# 3. Indexing and Slicing of NumPy Arrays

import numpy as np

matrix = np.random.randint(10, 51, size=(5, 5))
matrix[0, :] = 100
print(matrix)

#output:-

#without replacing :-

# [[10 28 29 46 11]
#  [13 48 46 48 15]
#  [49 47 50 46 24]
#  [48 22 37 22 28]
#  [36 37 28 41 17]]

# replace the ele in 1st row with 100:-

# [[100 100 100 100 100]
#  [ 20  47  25  39  11]
#  [ 24  15  50  33  34]
#  [ 25  35  50  25  29]
#  [ 11  16  13  47  49]]
