# 2. Combining and Splitting Arrays  
import numpy as np

arr1 = np.array([[1, 2],
                 [3, 4]]) 
arr2 = np.array([[5, 6],
                 [7, 8]])

# vstack :- adds rows
v_stacked = np.vstack((arr1, arr2))
print("Vertical Stack:\n", v_stacked)
# hstack :- add coloumns
h_stacked = np.hstack((arr1, arr2))
print("Horizontal Stack:\n", h_stacked)   
#vsplit :- split array rows ke sath me 
v_split = np.vsplit(v_stacked, 2)
print("Vertical Split:")
for part in v_split:
    print(part)
#hsplit :- split array columns ke sath me
h_split = np.hsplit(h_stacked, 2)
print("Horizontal Split:")
for part in h_split:
    print(part)

#output:-
# Vertical Stack:
#  [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]
# Horizontal Stack:
#  [[1 2 5 6]
#  [3 4 7 8]]
# Vertical Split:
# [[1 2]
#  [3 4]]
# [[5 6]
#  [7 8]]
# Horizontal Split:
# [[1 2]
#  [3 4]]
# [[5 6]
#  [7 8]]