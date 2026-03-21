# Task 4.1: Exploring a Series

import pandas as pd

fruits = ['apple','banana','cherry','date']
series = pd.Series(fruits)
print(series)
print()
print("number of elements:\n", series.size)
print("unique value:\n",series.unique())
print("count unique value:\n",series.value_counts())

#output:-
# 0     apple
# 1    banana
# 2    cherry
# 3      date
# dtype: object

# Size:
#  4
# unique value:
#  ['apple' 'banana' 'cherry' 'date']
# count unique value:
#  apple     1
# banana    1
# cherry    1
# date      1
# Name: count, dtype: int64


