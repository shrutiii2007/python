from functools import reduce

words = ["burhanpur", "khandwa", "indore", "bhopal"]

longest = reduce(lambda x, y: x if len(x) > len(y) else y, words)
print(longest)


# output:-

# burhanpur

