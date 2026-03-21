import matplotlib.pyplot as plt

months = list(range(1, 13))

product_A = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
product_B = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
product_C = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]

plt.stackplot(
    months,
    product_A,
    product_B,
    product_C,
    labels=['Product A', 'Product B', 'Product C']
)

plt.title("Monthly Sales of Products")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend(loc='upper left')
plt.show()
