#Task 5:  Joining DataFrames

#task 5.1

import pandas as pd

print("TWO DATAFRAMES MANUALLY:-")

df_grades = pd.DataFrame({
    'student_id': [101, 102, 103, 104, 105],
    'grade': ['A', 'B', 'A', 'C', 'B']
})

df_activities = pd.DataFrame({
    'student_id': [102, 103, 104, 106],
    'activity': ['Sports', 'Music', 'Dance', 'Drama']
})

print("1st dataframe:-\n",df_grades)
print("2nd dataframe:-\n",df_activities)

print("----------------------------------------------------------")

#task 5.2

print("JOIN THEM USING LEFT JOIN:-")

left_df = pd.merge(df_grades, df_activities, on='student_id', how='left')
print(left_df)

print("----------------------------------------------------------")

#task 5.3

print("JOIN THEM USING RIGHT JOIN:-")

right_df = pd.merge(df_grades, df_activities, on='student_id', how='right')
print(right_df)

print("----------------------------------------------------------")












