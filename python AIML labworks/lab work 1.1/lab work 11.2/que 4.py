s = "python"

try:
    print(s[10])
except IndexError:
    print("Error: string index out of range.")
else:
    print("character:",s[10])

# output:-
# Error: string index out of range.