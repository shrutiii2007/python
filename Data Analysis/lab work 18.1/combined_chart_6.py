import matplotlib.pyplot as plt

# Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
revenue = [5000, 7000, 6500, 8000, 7500, 9000]
profit = [1200, 1800, 1600, 2200, 2000, 2500]

# Create figure and first axis (Bar chart)
fig, ax1 = plt.subplots(figsize=(8, 5))

ax1.bar(months, revenue)
ax1.set_xlabel('Months')
ax1.set_ylabel('Revenue ($)')
ax1.set_title('Revenue and Profit Over 6 Months')

# Create second axis (Line chart)
ax2 = ax1.twinx()
ax2.plot(months, profit, marker='o')
ax2.set_ylabel('Profit ($)')

# Show grid only for bar axis
ax1.grid(True, axis='y')

plt.tight_layout()
plt.show()
