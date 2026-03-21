# 3. Groupby() and Transform()

import pandas as pd

orders = pd.DataFrame({
    'customer_id': [101, 101, 102, 103, 102],
    'order_amount': [500, 1200, 800, 1500, 2000]
})

print(orders)

print("----------------------------------------------")


max_order = orders.groupby('customer_id')['order_amount'].max()
print(max_order)


