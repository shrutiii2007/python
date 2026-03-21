# 2. Re-Indexing & Altering Labels

import pandas as pd

df = pd.DataFrame({
    "emp_name": ["Amit", "Neha"],
    "emp_sal": [50000, 60000]
})

print(df)

print("--------------------------------------------")

df_renamed = df.rename(columns={
    "emp_name": "Employee Name",
    "emp_sal": "Salary (INR)"
})

print(df_renamed)

print("--------------------------------------------")

