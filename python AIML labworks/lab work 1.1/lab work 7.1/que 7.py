def show_students(*students):
    if not students:
        print("No student names provided.")
    else:
        for name in students:
            print(name)

show_students("Amit", "Neha", "Ravi")
# show_students()
#agar name provide kiye ho toh ye ayega
# Amit
# Neha
# Ravi
# or agar nhi kiye hoge to
# No student names provided.
