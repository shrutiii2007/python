def greet(name):
    print("Hello", name)

if __name__ == "__main__":
    print("This script is executed directly.")
    greet("Student")
else:
    print("This script is imported as a module.")


# output:-
# This script is executed directly.
# Hello Student