import numpy as np

scores = np.array([65, 80, 72, 90, 55, 78])

grades = np.where(scores >= 75, 'Pass', 'Fail')

print(grades)

# output:-

# ['Fail' 'Pass' 'Fail' 'Pass' 'Fail' 'Pass']





