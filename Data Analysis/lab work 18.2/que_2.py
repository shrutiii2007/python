import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

HR = [20, 25, 30, 28, 32, 35]
Marketing = [30, 35, 40, 38, 42, 45]
Sales = [50, 55, 60, 65, 70, 75]
IT = [40, 45, 50, 48, 52, 55]

plt.stackplot(
    months,
    HR,
    Marketing,
    Sales,
    IT,
    labels=['HR', 'Marketing', 'Sales', 'IT']
)

plt.title("Department-wise Revenue Distribution")
plt.xlabel("Months")
plt.ylabel("Revenue")
plt.legend(loc='upper left')
plt.show()
