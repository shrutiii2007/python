def reverse(s):
    if len(s) <= 1:
        return s
    
    return s[-1] + reverse(s[:-1])

text = input("Enter a string: ")
print("Reversed string:", reverse(text))

# output is :- 
# Enter a string: 2 4 6 8 12 45 63 20 
# Reversed string:  02 36 54 21 8 6 4 2

