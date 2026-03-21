import pandas as pd

# Task 6: Complex Merging

#task 6.1

print("LOAD TWO DATASETS USING COMMON COLOUMNS:-")

orders_df = pd.read_csv("orders.csv")
customers_df = pd.read_csv("customer.csv")

print("Orders Dataset:")
print(orders_df.head())

print("\nCustomers Dataset:")
print(customers_df.head())

print("----------------------------------------------------------")

#task 6.2

print("MERGE THEM TO GET CUSTOMER DETAILS ALONGSIDE THEIR ORDERS:-")

merged_df = pd.merge(orders_df, customers_df, on='CustomerID', how='left')

# Display the merged dataframe
print(merged_df)

print("----------------------------------------------------------")

# Task 6.3 

print("HIGH-VALUE CUSTOMERS (TotalOrderValue > 1000):")

customer_totals = merged_df.groupby(
    ['CustomerID', 'CustomerName', 'Email', 'JoinDate', 'Country'],
    as_index=False
)['TotalOrderValue'].sum()

high_value_customers = customer_totals[customer_totals['TotalOrderValue'] > 1000]

print(high_value_customers)

print("----------------------------------------------------------")

# John Doe: 250 + 500 + 600 = 1350 ✅
# Jane Smith: 150 + 120 = 270 ❌
# Bob Johnson: 300 + 700 = 1000 ✅
# Alice Brown: 200 ❌
# Charlie Davis: 450 + 350 = 800 ❌








