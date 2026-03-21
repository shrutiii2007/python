a = int(input("enter the first number :-"))
b = int(input("enter the second number :-"))
c = int(input("enter the third number :-"))
d = int(input("enter the fourth number :-"))

if a > b:
    if a > c:
        if a > d:
            print("Maximum is:", a)
        else:
            print("Maximum is:", d)
    else:
        if c > d:
            print("Maximum is:", c)
        else:
            print("Maximum is:", d)
else:
    if b > c:
        if b > d:
            print("Maximum is:", b)
        else:
            print("Maximum is:", d)
    else:
        if c > d:
            print("Maximum is:", c)
        else:
            print("Maximum is:", d)


# output:-
# enter the first number :-20
# enter the second number :-30
# enter the third number :-40
# enter the fourth number :-50
# Maximum is: 50