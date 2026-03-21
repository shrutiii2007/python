# Task 3.3: Creating a DataFrame 
# from a NumPy Array

import numpy as np
import pandas as pd

data_array = np.random.randint(1, 11, size=(3, 2))

random_df = pd.DataFrame(data_array, columns=['Column A', 'Column B'])

print(random_df)

#output:-
#    Column A  Column B
# 0         3         4
# 1        10         6
# 2         6         6


