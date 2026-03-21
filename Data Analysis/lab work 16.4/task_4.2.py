# Task 4.2: Exploring a DataFrame

import pandas as pd

student_data = {
'name': ['Alice', 'Bob', 'Charlie'],
'age': [20, 21, 19],
'major': ['CS', 'Engineering', 'Math']
}

df = pd.DataFrame(student_data)
print(df)
print()
print("first 2 rows:-\n",df.head(2))
print()
print("last row:-\n",df.tail(1))
print()
print("index:-\n",df.index)
print()
print("columns name:-\n",df.columns)
print()
print("concise summary:-\n",df.info())



