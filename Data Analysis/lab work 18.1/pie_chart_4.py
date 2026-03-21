import matplotlib.pyplot as plt

# Data
fruits = ["Apples", "Bananas", "Oranges", "Grapes", "Mangoes"]
sales = [30, 25, 20, 15, 10]   # percentages

# Create pie chart
plt.figure(figsize=(6, 6))
plt.pie(
    sales,
    labels=fruits,
    autopct='%1.1f%%',
    startangle=90
)

# Title
plt.title("Percentage Distribution of Fruits Sold")

# Equal aspect ratio makes the pie circular
plt.axis('equal')

# Display chart
plt.show()
