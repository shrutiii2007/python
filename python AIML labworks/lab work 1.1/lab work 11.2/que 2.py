list = [10,20,30]

try:
    print(list[5])
except IndexError:
    print("Error :- index out of range")

# output:-
# Error :- index out of range