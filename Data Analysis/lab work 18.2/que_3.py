import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
sales = [50, 60, 70, 80, 90]
profit = [10, 15, 20, 25, 30]

fig, axs = plt.subplots(1, 2, figsize=(10, 4))

# Bar Plot
axs[0].bar(x, sales)
axs[0].set_title("Sales")
axs[0].set_xlabel("Month")
axs[0].set_ylabel("Sales Value")

# Line Plot
axs[1].plot(x, profit, marker='o')
axs[1].set_title("Profit")
axs[1].set_xlabel("Month")
axs[1].set_ylabel("Profit Value")

plt.tight_layout()
plt.show()
