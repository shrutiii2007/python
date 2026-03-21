from functools import reduce

words = ["my", "name", "is", "shruti","Bhawsar"]

sentence = reduce(lambda x, y: x + " " + y, words)
print(sentence)


# output:-

# my name is shruti Bhawsar

