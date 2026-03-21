# Task 4.3: Selecting Columns and Rows

import pandas as pd

employee_data = [{'name': 'David', 'salary': 50000, 'department': 'Sales'},
{'name': 'Eve', 'salary': 60000, 'department': 'Marketing'},
{'name': 'Frank', 'salary': 55000, 'department': 'Sales'}]

df = pd.DataFrame(employee_data)
print(df)
print("Select and print only the 'name' column.")
print(df["name"]) 
print(" Select and print the row at index 1.")
print(df.loc[1])
print("Select and print the 'name' and 'salary' columns.")
print(df[['name', 'salary']])
print(" Select and print the first two rows and the 'name' and 'department' columns.")
print(df.loc[0:1, ['name', 'department']])

