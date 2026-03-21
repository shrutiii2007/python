file = open("sample.txt","r")
for line in file:
    print(line.strip())
file.close()

# output:-
# learning file handling in python is fun!