#1
A=int(input("Enter your first number:"))
B=int(input("Enter your secound number:"))
C=int(input("Enter your third number:"))
if A < B:
    if A < C:
        print("Minimum is:", A)
    else:
        print("Minimum is:", C)
else:
    if B < C:
        print("Minimum is:", B)
    else:
        print("Minimum is:", C)
print()


#2

A=int(input("Enter your first number:"))
B=int(input("Enter your secound number:"))
C=int(input("Enter your third number:"))
D=int(input("Enter your fourth number:"))

if A > B:
    if A > C:
        if A > D:
            print("Maximum is:", A)
        else:
            print("Maximum is:", D)
    else:
        if C > D:
            print("Maximum is:", C)
        else:
            print("Maximum is:", D)
else:
    if B > C:
        if B > D:
            print("Maximum is:", B)
        else:
            print("Maximum is:", D)
    else:
        if C > D:
            print("Maximum is:", C)
        else:
            print("Maximum is:", D)
#3            
A=int(input("Enter a number:"))
if A>=0:
    if A==0:
        print("A is Zero")
    else:
        print("Positive")
else:
    print("Negeative")
#4


marks=int(input("Enter your marks:"))
print("pass") if marks>=40 else print("Fail")
#5
oddandeven=int(input("Enter A number:"))
print("Even") if oddandeven % 2  ==0 else ("odd")
