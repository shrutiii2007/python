import pandas as pd

hours = pd.DataFrame({
    "Department": ["IT", "IT", "HR", "HR", "IT"],
    "Project": ["A", "B", "A", "B", "A"],
    "Hours": [40, 35, 30, 25, 45]
})
print(hours)

print("---------------------------------------")

pivot_hours = pd.pivot_table(
    hours,
    index="Department",
    columns="Project",
    values="Hours",
    aggfunc="sum"
)

print(pivot_hours)


