# Task 3.2: Creating a DataFrame from a
# List of Dictionaries

import pandas as pd

data = [{'name': 'David', 'salary': 50000, 'department': 'Sales'},
{'name': 'Eve', 'salary': 60000, 'department': 'Marketing'},
{'name': 'Frank', 'salary': 55000, 'department': 'Sales'}]


df = pd.DataFrame(data)
print(df)

#output:-
#     name  salary department
# 0  David   50000      Sales
# 1    Eve   60000  Marketing
# 2  Frank   55000      Sales


