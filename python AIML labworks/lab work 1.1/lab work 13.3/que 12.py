words = ["indore", "goa", "isanpur", "pune"]

long_words = list(filter(lambda x: len(x) > 5, words))
print(long_words)


# output:-
# ['indore', 'isanpur']
