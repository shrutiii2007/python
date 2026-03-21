filename=input("enter filename :-")

try:
    file=open(filename,"r")
except FileNotFoundError:
    print("Error: file not found.")
else:
    print("file content:")
    print(file.read())
    file.close()


# output:-
# enter filename :-notes.txt
# file content:
# line 1: python is easy to learn.
# line 2: it has numerous libraries.
# line 3: file handling is one of its features.
# line 4: Python supports multiple modes of file handling!