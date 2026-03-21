from datetime import datetime

year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")


# output:-

# Enter year: 2023
# 2023 is not a Leap Year

# Enter year: 2024
# 2024 is a Leap Year