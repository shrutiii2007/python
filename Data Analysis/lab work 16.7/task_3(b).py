# 3. Groupby() and Transform()

import pandas as pd

students = pd.DataFrame({
    'class': ['10A', '10A', '10B', '10B', '10C'],
    'marks': [85, 78, 90, 88, 92]
})

avg_marks = students.groupby('class')['marks'].mean()
print(avg_marks)







