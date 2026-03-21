# 2. Re-Indexing & Altering Labels

import pandas as pd

inventory = pd.DataFrame({
    "Product": ["Laptop", "Phone", "Tablet"],
    "Stock": [15, 30, 20]
}, index=["P101", "P102", "P103"])

print("Original DataFrame:")
print(inventory)

# Reset index and keep old index
inventory_reset = inventory.reset_index()
inventory_reset.rename(columns={"index": "ProductID"}, inplace=True)

print("\nAfter reset_index():")
print(inventory_reset)



