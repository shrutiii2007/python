import matplotlib.pyplot as plt

# Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [450, 520, 610, 580, 700, 650]

# Create line chart
plt.figure(figsize=(8, 5))
plt.plot(months, sales, marker='o')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.title('Monthly Sales Trend')

# Find highest and lowest points
max_value = max(sales)
min_value = min(sales)

max_index = sales.index(max_value)
min_index = sales.index(min_value)

# Annotate highest point
plt.annotate(
    f'Highest: {max_value}',
    xy=(months[max_index], max_value),
    xytext=(months[max_index], max_value + 40),
    arrowprops=dict(arrowstyle='->')
)

# Annotate lowest point
plt.annotate(
    f'Lowest: {min_value}',
    xy=(months[min_index], min_value),
    xytext=(months[min_index], min_value - 60),
    arrowprops=dict(arrowstyle='->')
)

# Grid
plt.grid(True)

plt.tight_layout()
plt.show()
