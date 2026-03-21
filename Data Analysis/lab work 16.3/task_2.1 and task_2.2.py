import numpy as np

# task 2.1

temperatures = np.array([28, 32, 25, 35, 30, 22, 38])

is_hot = temperatures > 30

hot_temperatures = temperatures[is_hot]

print("Temperatures array:", temperatures)
print("Boolean mask (is_hot):", is_hot)
print("Hot temperatures:", hot_temperatures)

# Temperatures array: [28 32 25 35 30 22 38]
# Boolean mask (is_hot): [False  True False  True False False  True]
# Hot temperatures: [32 35 38]

#task 2.2

temperatures = np.array([28, 32, 25, 35, 30, 22, 38])

is_hot = temperatures > 30

temperatures[is_hot] = 31

print("Updated temperatures:", temperatures)

# Updated temperatures: [28 31 25 31 30 22 31]


