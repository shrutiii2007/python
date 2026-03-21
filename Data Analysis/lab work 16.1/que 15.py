# 3. Indexing and Slicing of NumPy Arrays

import numpy as np

arr = np.array([1, 3, 5, 7, 2, 9, 4, 6, 8, 0])
filtered_arr = arr[arr > 5]
# numpy check krega har element ko or boolean value return krega
#sirf vhi elements jo true ho select hoge
print(filtered_arr)

#output:-
# [7 9 6 8]
