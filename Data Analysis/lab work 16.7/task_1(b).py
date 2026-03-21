import pandas as pd

marks = pd.DataFrame({
    "Student": ["Amit", "Amit", "Neha", "Neha", "Ravi", "Ravi"],
    "Subject": ["Math", "Science", "Math", "Science", "Math", "Science"],
    "Marks": [85, 90, 78, 88, 92, 81]
})

print(marks)
print("---------------------------------------")
pivot_marks = marks.pivot(index="Student", columns="Subject", values="Marks")
print(pivot_marks)
