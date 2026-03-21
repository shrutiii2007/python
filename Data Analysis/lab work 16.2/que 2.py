# 1. Mathematical Operations
import numpy as np

arr = np.random.randint(0, 5, size=4)

print(arr)
print("Square Root:", np.sqrt(arr)) 
print("Exponential:", np.exp(arr))
print("Logarithm (base e):", np.log(arr))

# 2. Generate a NumPy array with random integers and apply 
# square root, exponential, and logarithmic functions.

#output:-
# [1 1 3 2]
# Square Root: [1.         1.         1.73205081 1.41421356]
# Exponential: [ 2.71828183  2.71828183 20.08553692  7.3890561 ]
# Logarithm (base e): [0.         0.         1.09861229 0.69314718]

