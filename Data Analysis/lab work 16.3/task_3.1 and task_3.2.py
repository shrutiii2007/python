import numpy as np

#TASK 3.1

print("----1D array into 2D array----")

numbers_1d = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

print("array:-" + str(numbers_1d))

numbers_2d = np.reshape(numbers_1d, (3, 4))

print("before reshaped 1d array:-\n",numbers_1d)

print("after Reshaped into 2d Array:-\n")
print(numbers_2d)

#TASK 3.2

reshaped = numbers_2d.flatten()
print("reshaped into 1D array using flatten:-\n",reshaped)

#output:-
# ----1D array into 2D array----
# array:-[ 1  2  3  4  5  6  7  8  9 10 11 12]
# before reshaped 1d array:-
#  [ 1  2  3  4  5  6  7  8  9 10 11 12]
# after Reshaped into 2d Array:-

# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
# reshaped into 1D array using flatten:-
#  [ 1  2  3  4  5  6  7  8  9 10 11 12]




