# Question:-1

a= int(input("Enter your number:"))
print(a%2==0)
if a%2==1:
    print("Even")
else:
    print("Odd")


# Question:- 2

A = int(input("Enter your First number:"))
B = int(input("Enter your Second number:"))

if A>B:
           print("A is Greater than B:")
else:
    print("B is Greater than A:")


# Question:-3

num = int(input("Enter your number:"))
if num>0:
          print("your number is positive")

elif num<0:
    print("your number is nagative")

else:
    print("your number is zero")


# Question:-4

A = int(input("Enter your first number:"))
B = int(input("Enter your second number:"))
C = int(input("Enter your third number:"))

if A>=B and A>=C:
        print("The largest number is A",A)
elif B>=A and B>=C:
        print("The largest number is B",B)
else:
   print("The largest number is C",C)


# Question:-5

Num1=int(input("Enter your first number:"))
Num2=int(input("Enter your secound number:"))
op=input("Enter Operator like (+,-,*,/):")
if op =='+':
    print("Result:",Num1 + Num2)
elif op =='-':
    print("Result:" ,Num1 - Num2)
elif op =='*':
    print("Result:",Num1 * Num2)
elif op =='/':
    print("Result:",Num1 / Num2)
else:
    print("Invled operator")
