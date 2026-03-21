import matplotlib.pyplot as plt

# Data
months = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

temperatures = [15, 17, 22, 28, 33, 36, 35, 34, 30, 25, 20, 16]

# Create line chart
plt.figure(figsize=(8, 5))
plt.plot(months, temperatures, marker='o')

# Labels and title
plt.xlabel("Months")
plt.ylabel("Temperature (°C)")
plt.title("Monthly Temperature Changes in a City")

# Show grid
plt.grid(True)

# Display chart
plt.show()



