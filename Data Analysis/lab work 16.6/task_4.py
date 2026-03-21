# Task 4: Merging DataFrames

#task 4.1

import pandas as pd

print("TWO SMALL DATAFRAMES MANUALLY:-")

df1 = pd.DataFrame({
    'Employee_ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David']
})

df2 = pd.DataFrame({
    'Employee_ID': [3, 4, 5, 6],
    'Salary': [50000, 60000, 70000, 80000]
})

print("1st DataFrame:-\n", df1)
print("2nd DataFrame:-\n", df2)

print("----------------------------------------------------------")

#task 4.2

print("MERGE USING INNER JOIN:-")
inner_df = pd.merge(df1, df2, on='Employee_ID', how='inner')
print(inner_df)
print("----------------------------------------------------------")

#task 4.3

print("MERGE USING OUTER JOIN:-")
outer_df = pd.merge(df1, df2, on='Employee_ID', how='outer')
print(outer_df)
print("----------------------------------------------------------")