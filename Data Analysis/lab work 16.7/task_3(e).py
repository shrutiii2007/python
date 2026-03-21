# 3. Groupby() and Transform()

import pandas as pd

employees = pd.DataFrame({
    'department': ['IT', 'IT', 'HR', 'HR', 'Finance', 'Finance'],
    'salary': [60000, 65000, 50000, 52000, 70000, 72000]
})

employees['salary_standardized'] = (
    employees.groupby('department')['salary']
    .transform(lambda x: (x - x.mean()) / x.std())
)

print(employees)


