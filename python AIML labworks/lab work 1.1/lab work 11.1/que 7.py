file = open("sample.txt","r")
text = file.read()
file.close()

lines=text.splitlines()
words=text.split()
charcters=len(text)

print("lines:",len(lines))
print("words:",len(words))
print("charcters:",charcters)

# output:-
# lines: 1
# words: 7
# charcters: 40