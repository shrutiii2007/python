# 1. Reading and Writing CSV, JSON, and Excel Files

import pandas as pd
#TASK 1
print("Task 1: Read CSV\n")
df = pd.read_csv("sample_data.csv")
print(df)
df.info()

print("----------------------------------")
#TASK 2
print("Task 2: Save to Excel\n")
df.to_excel("output_data.xlsx", index=False)

print("----------------------------------")
#TASK 3
print("Task 3: Read JSON")
df = pd.read_csv("sample_data.csv")
df.to_json("sample_data.json", orient="records", indent=4)

print("----------------------------------")
#TASK 4
print("Task 4: Export DataFrame to JSON")
df.to_json("export_data.json", orient="records", indent=4)

print("----------------------------------")

