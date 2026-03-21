num = int(input("Enter a number: "))

if num < 0:
    raise ValueError("Negative number is not allowed")
else:
    print("Valid number:", num)

# output:-

# Enter a number: 34
# Valid number: 34

# Enter a number: -10
# raise ValueError("Negative number is not allowed")
# ValueError: Negative number is not allowed