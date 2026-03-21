#dice roll

import random

dice = random.randint(1, 6)
print("Dice rolled:", dice)

#shuffle a list

import random

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)

print("Shuffled list:", numbers)

# output:-

# 1 st time run:-
# Dice rolled: 1
# Shuffled list: [5, 1, 2, 3, 4]

# 2 nd time run:-
# Dice rolled: 5
# Shuffled list: [4, 5, 1, 3, 2]