# Task 5.1: Adding a New Column
import pandas as pd

student_data = {
'name': ['Alice', 'Bob', 'Charlie'],
'age': [20, 21, 19],
'major': ['CS', 'Engineering', 'Math']
}
df = pd.DataFrame(student_data)
print(df)
print("updated dataframe with new coloumn :- city")
df["city"] = ["New York","London","Paris"]
print(df)

# Task 5.2: Removing a Column

print("DataFrame after removal of city:-")
df = df.drop(columns=['city'])
print(df)
