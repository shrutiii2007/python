import pandas as pd

# Load datasets
orders_df = pd.read_csv("orders.csv")
customers_df = pd.read_csv("customer.csv")

# Merge datasets
merged_df = pd.merge(orders_df, customers_df, on='CustomerID', how='left')

# Convert OrderDate to datetime
merged_df['OrderDate'] = pd.to_datetime(merged_df['OrderDate'])

# Extract Year-Month as clean string
merged_df['YearMonth'] = merged_df['OrderDate'].dt.strftime('%Y-%m')

# ✅ Group by YearMonth and sum TotalOrderValue
monthly_summary = merged_df.groupby('YearMonth', as_index=False).agg({'TotalOrderValue': 'sum'})

print("Total Order Value by Month:")
print(monthly_summary)
