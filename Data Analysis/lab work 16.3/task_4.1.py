import numpy as np

prices = np.array([10,20,30])

result = prices + 5

print("original array:-",prices)

print("Broadcasted array:-",result)

#output:-
# original array:- [10 20 30]
# Broadcasted array:- [15 25 35]


