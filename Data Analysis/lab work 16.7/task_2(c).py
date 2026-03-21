# 2. Re-Indexing & Altering Labels

import pandas as pd

customers = pd.DataFrame({
    "Purchase": [2500, 3400, 1800]
}, index=["alice", "bob", "charlie"])

print("Original Index:")
print(customers)

print("--------------------------------------------")

# Convert index to uppercase
customers.index = customers.index.str.upper()

print("\nUppercase Index:")
print(customers)






