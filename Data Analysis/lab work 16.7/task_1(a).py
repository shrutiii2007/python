import pandas as pd

sales = pd.DataFrame({
    "Month": ["Jan", "Jan", "Feb", "Feb", "Mar", "Mar"],
    "Product": ["Laptop", "Phone", "Laptop", "Phone", "Laptop", "Phone"],
    "Sales": [50000, 30000, 55000, 32000, 60000, 35000]
})

print(sales)
print("---------------------------------------")

pivot_sales = sales.pivot(index="Month", columns="Product", values="Sales")
print(pivot_sales)
