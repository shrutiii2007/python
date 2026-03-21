import matplotlib.pyplot as plt

ages = [18, 19, 20, 21, 22, 23]
students = [5, 12, 18, 10, 6, 4]

plt.bar(ages, students)
plt.title("Age Distribution of Students")
plt.xlabel("Age")
plt.ylabel("Number of Students")

plt.savefig("age_distribution.png")
plt.show()
