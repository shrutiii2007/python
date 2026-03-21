words = ["apple", "kiwi", "banana", "grape"]

print("By length:", sorted(words, key=lambda x: len(x)))
print("By last letter:", sorted(words, key=lambda x: x[-1]))


# output:-

# By length: ['kiwi', 'apple', 'grape', 'banana']
# By last letter: ['banana', 'apple', 'grape', 'kiwi']

