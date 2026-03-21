import numpy as np

values = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

print("1D array:-\n",values)

reshape = values.reshape(5,-1)

print("2D array:-\n",reshape)

# output:-
# 1D array:-
#  [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]
# 2D array:-
#  [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]
#  [13 14 15]]

