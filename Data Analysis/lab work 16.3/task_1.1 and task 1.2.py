import numpy as np

#task 1.1

ages = np.array([25, 30, 18, 35, 22, 40, 17])

adults = ages[ages >= 18]

print("Ages:", ages)
print("Adults:", adults)

# output:-
# Ages: [25 30 18 35 22 40 17]
# Adults: [25 30 18 35 22 40]

#task 1.2

young_adults = ages[(ages > 20) & (ages < 35)]

print("Young Adults:", young_adults)

# output:-
# Young Adults: [25 30 22]



