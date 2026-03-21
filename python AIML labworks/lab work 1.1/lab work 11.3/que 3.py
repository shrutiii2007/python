age = int(input("Enter your age: "))

try:
    assert age > 18, "Age must be above 18"
    print("Access granted")
except AssertionError as e:
    print("Error:", e)

# output:-

# Enter your age: 22
# Access granted

# Enter your age: 17
# Error: Age must be above 18