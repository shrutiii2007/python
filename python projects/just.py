import matplotlib.pyplot as plt

# Data
ad_spend = [5, 6, 7, 6, 8, 7.5, 9, 10, 9.5, 11, 10.5, 12]
sales = [40, 45, 50, 46, 54, 53, 58, 62, 59, 65, 64, 70]
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

# Create Scatter Plot
plt.figure(figsize=(10,6))
plt.scatter(ad_spend, sales, color='darkorange', edgecolors='black', s=100)

# Annotate points with month names
for i in range(len(months)):
    plt.text(ad_spend[i]+0.1, sales[i], months[i], fontsize=9)

# Labels & Title
plt.title("Ad Spend vs Sales", fontsize=16)
plt.xlabel("Advertisement Spend ($1000s)", fontsize=12)
plt.ylabel("Sales ($1000s)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()