# 3. Search, Sort, Aggregating/Statistical Functions

import numpy as np

arr = np.array([10, 25, 30, 15, 40])

result = np.where(arr > 20)
print(result)
  
# (array([1, 2, 4]),)             ye index number hai

print(arr[result])

# [25 30 40]
 

