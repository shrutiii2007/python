import numpy as np

arr = np.array([10, -5, 0, 7, -2, 0, 3])

positive = np.sum(arr > 0)
negative = np.sum(arr < 0)
zero = np.sum(arr == 0)

print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)

# arr > 0 → gives True / False
# True = 1, False = 0
# np.sum() adds them → count


# output:-
# Positive: 3
# Negative: 2
# Zero: 2



