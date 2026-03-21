class InvalidGradeError(Exception):
    pass

grade = input("Enter grade: ")

try:
    assert grade != "", "Grade cannot be empty"
    grade = int(grade)

    if grade < 0 or grade > 100:
        raise ValueError("Grade must be between 0 and 100")

    if grade < 40:
        raise InvalidGradeError("Failing grade")

    print("Grade accepted")

except (AssertionError, ValueError, InvalidGradeError) as e:
    print("Error:", e)


# output:-

# Enter grade: 78
# Grade accepted

# Enter grade: 23
# Error: Failing grade

# Enter grade: shruti
# Error: invalid literal for int() with base 10: 'shruti'

# Enter grade: -12
# Error: Grade must be between 0 and 100

# Enter grade: 
# Error: Grade cannot be empty
