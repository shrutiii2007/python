# Task 3.1: Creating a DataFrame from a
# Dictionary of Lists

import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [20, 21, 19],
    "major": ["CS", "Engineering", "Math"]
}

df = pd.DataFrame(data)
print(df)

#output:-
    #   Name  Age        major
# 0    Alice   20           CS
# 1      Bob   21  Engineering
# 2  Charlie   19         Math

