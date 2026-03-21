import pandas as pd
import matplotlib.pyplot as plt

#Task 8: Challenge Task

# task 8.1

print("THREE SAMLL DATASETS:-")

products = pd.DataFrame({
    'ProductID': [1, 2, 3],
    'ProductName': ['Laptop', 'Mobile', 'Headphones']
})

sales = pd.DataFrame({
    'ProductID': [1, 2, 3],
    'TotalSales': [50000, 30000, 10000]
})

returns = pd.DataFrame({
    'ProductID': [1, 2, 3],
    'TotalReturns': [5000, 2000, 1000]
})

print("PRODUCT DATAFRAME:-\n",products)
print("SALES DATAFRAME:-\n",sales)
print("RETURNS DATAFRAME:-\n",returns)

print("----------------------------------------------------------")

#task 8.2

print("MERGE THEM LOGICALLY:-")

merged_data = products.merge(sales, on='ProductID') .merge(returns, on='ProductID')
print(merged_data)

print("----------------------------------------------------------")

#task 8.3

print("FIMAL REPORT:-")

merged_data['NetSales'] = merged_data['TotalSales'] - merged_data['TotalReturns']

print(merged_data)

print("----------------------------------------------------------")

#task 8.4

print("VISUALIZE THE NET SALES PER PRODUCT USING A BAR CHART:-")

plt.bar(merged_data['ProductName'], merged_data['NetSales'])
plt.xlabel('Product')
plt.ylabel('Net Sales')
plt.title('Net Sales per Product')
plt.show()

print("----------------------------------------------------------")



