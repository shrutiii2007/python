num_1 = int(input("enter the first number :-"))
num_2 = int(input("enter the second number :-"))
num_3 = int(input("enter the third number :-"))

if num_1>num_2 :
    if num_1>num_3:
        print("maximum is first:", num_1)
    else:
        print("maximum is third:", num_3)
else:
    if num_2 > num_3:
        print("Maximum is second:", num_2)
    else:
        print("Maximum is third:", num_3)


# output:-
# enter the first number :-20
# enter the second number :-10
# enter the third number :-30
# maximum is: 30