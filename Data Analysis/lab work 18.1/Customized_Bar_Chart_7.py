import matplotlib.pyplot as plt

# Data
categories = ['Electronics', 'Clothing', 'Groceries', 'Books', 'Toys']
sales = [850, 620, 980, 430, 560]

# Create bar chart
plt.figure(figsize=(8, 5))
bars = plt.bar(
    categories,
    sales,
    color=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0'],
    edgecolor='black'
)

# Labels and title
plt.xlabel('Product Category', fontsize=12)
plt.ylabel('Sales ($)', fontsize=12)
plt.title('Sales by Product Category', fontsize=14)

# Grid lines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Value labels on bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height + 15,
        f'{height}',
        ha='center',
        fontweight='bold'
    )

# Layout adjustment
plt.tight_layout()
plt.show()

