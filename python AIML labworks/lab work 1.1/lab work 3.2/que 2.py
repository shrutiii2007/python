a = int(input("enter the first number :-"))
b = int(input("enter the second number :-"))
c = int(input("enter the third number :-"))

if a<b :
    if a<c:
        print("A is minimum")
    else:
        print("minimum is:", c)
else:
    if b < c:
        print("Minimum is:", b)
    else:
        print("Minimum is:", c)


# output:-
# enter the first number :-23
# enter the second number :-34
# enter the third number :-45
# A is minimum