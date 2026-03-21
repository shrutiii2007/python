# 3. Search, Sort, Aggregating/Statistical Functions

import numpy as np

arr = np.random.randint(0, 5, size=4)
print(arr)

print("Mean:-",np.mean(arr))
print("Median:-",np.median(arr))
print("variance:-",np.var(arr))
print("Standard Deviation:-",np.std(arr))

#output:-
# [1 0 2 2]
# Mean:- 1.25
# Median:- 1.5
# variance:- 0.6875
# Standard Deviation:- 0.82915619758885

