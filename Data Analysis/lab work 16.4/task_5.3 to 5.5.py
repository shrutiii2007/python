# Task 5.3: Filtering Rows Based on a Condition
import pandas as pd

employee_data = [{'name': 'David', 'salary': 50000, 'department': 'Sales'},
{'name': 'Eve', 'salary': 60000, 'department': 'Marketing'},
{'name': 'Frank', 'salary': 55000, 'department': 'Sales'}]

df = pd.DataFrame(employee_data)
print(df)

print("only print 'department' is 'Sales'.")
sales_df = df[df['department'] == 'Sales']
print(sales_df)

# Task 5.4: Sorting a DataFrame
print("salary column in descending order.")
df = df.sort_values("salary", ascending=False)
print(df)

# Task 5.5: Basic Aggregation
print("average salary of all employees.")
average_salary = df['salary'].mean()
print("Average salary:", average_salary)

