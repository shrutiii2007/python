for i in range(1, 51):
    if i % 2 == 0 and i % 3 == 0:
        print(i, "is Divisible by both 2 and 3")
    elif i % 2 == 0:
        print(i, "is Divisible by 2")
    elif i % 3 == 0:
        print(i, "is Divisible by 3")
    else:
        print(i, "is not divisible by 2 or 3")

# output :-

# 1 is not divisible by 2 or 3
# 2 is Divisible by 2
# 3 is Divisible by 3
# 4 is Divisible by 2
# 5 is not divisible by 2 or 3
# 6 is Divisible by both 2 and 3
# .
# .
# .
# 50 is Divisible by 2