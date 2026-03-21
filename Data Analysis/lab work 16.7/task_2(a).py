# 2. Re-Indexing & Altering Labels

import pandas as pd

employees = pd.DataFrame({
    "Name": ["Amit", "Neha", "Ravi"],
    "Department": ["IT", "HR", "Finance"]
})

print("Original DataFrame:")
print(employees)

print("--------------------------------------------")
# Re-index starting from 1001
employees.index = range(1001, 1001 + len(employees))

print("\nReindexed DataFrame:")
print(employees)

print("--------------------------------------------")

