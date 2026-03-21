file = open("sample.txt","r")
print(file.read())
file.close()

file=open("sample.txt","w")
file.write("learning file handling in python is fun!")
file.close()

# output:-
# learning file handling in python is fun!