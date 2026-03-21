# 3. Groupby() and Transform()
import pandas as pd

sales = pd.DataFrame({
    'region': ['East', 'West', 'East', 'South', 'West'],
    'sales': [2500, 3000, 1800, 2200, 3500]
})

print(sales)

print("-------------------------------------")

total_sales_region = sales.groupby('region')['sales'].sum()
print(total_sales_region)


