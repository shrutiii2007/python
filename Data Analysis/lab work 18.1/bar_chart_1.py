import matplotlib.pyplot as plt

# Sample dataset
products = ['Laptop', 'Smartphone', 'Headphones', 'Monitor', 'Keyboard']
sales = [1200, 950, 300, 450, 200]

# Create a vertical bar chart (Column chart)
plt.figure(figsize=(8,5))
plt.bar(products, sales, color='lightpink', edgecolor='black')

# Add title and labels
plt.title('Product-wise Sales', fontsize=14)
plt.xlabel('Product', fontsize=12)
plt.ylabel('Sales ($)', fontsize=12)

# Optional: add value labels on top of bars
for i, v in enumerate(sales):
    plt.text(i, v + 20, str(v), ha='center', fontweight='bold')

# Show plot
plt.tight_layout()
plt.show()


