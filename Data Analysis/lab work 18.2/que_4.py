import matplotlib.pyplot as plt

months = list(range(1, 13))

city1 = [15, 17, 20, 25, 30, 35, 37, 36, 32, 28, 22, 18]
city2 = [10, 12, 15, 20, 25, 30, 32, 31, 27, 23, 18, 14]
city3 = [20, 22, 25, 30, 35, 40, 42, 41, 37, 33, 27, 23]

plt.plot(months, city1, label='City A')
plt.plot(months, city2, label='City B')
plt.plot(months, city3, label='City C')

plt.title("Yearly Temperature Variation")
plt.xlabel("Months")
plt.ylabel("Temperature (°C)")
plt.legend(loc='upper left')
plt.show()
