import numpy as np

names = np.array(['Alice', 'Bob', 'Charlie', 'David', 'Eve'])

selected_names = names[np.char.startswith(names, 'A') | np.char.startswith(names, 'E')]

print("Selected Names:", selected_names)


# output:-
# Selected Names: ['Alice' 'Eve']



