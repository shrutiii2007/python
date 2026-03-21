name = input("enter your name:")
print(type(name))
age = input ("enter your age:")
print (type(age))
height = input("enter your height:")
print(type(height))
verify = (input("information is True/False:"))
print (type(verify))


print(" use of type casting construction")

#type construction

name = ("shruti")
print(name)
print(type(name))

age = 18
print(age)
print(type(age))

height = 145.7
print(height)
print(type(height))

verify = True
print(verify)
print(type(verify))

#que 2

float_number = float(input("enter your number:"))


int_number = int(float_number)
print( "your given number in float:",float_number)
print( "coversion of your number into integer:",int_number)

#question-3
a= bool(input("Enter Number:"))
print (type(a))
b= int(a)
print("Your number in integer:",b)
print(type(b))
c=str(a)
print("Your number in String:",c)
print(type(c))

#question-4

#string
p="abcd"
print(p)
print(type(p))

#Integer
q=-56487
print(q)
print(type(q))

#Float
r=87.41
print(r)
print(type(r))

#Boolean
t=False
print(t)
print(type(t))

#question-5

'''Calculations of Areas'''
#circle

print("Calculate the area of a circle.")
radius=float(input("Enter radius:"))
pi=3.14
area=pi *radius*radius
print("Formula of Area of circle=πr2")
print(f"Area of circle{radius} is:{area}")

#rectangle

print("Calculate the area of a Rectangle.")
l=float(input("Enter Length:"))
b=float(input("Enter Breath:"))
area=l*b
print("Formula of Area of Rectangle= Length*Breath")
print(f"The area of the rectangle is: {area}")
#square

print("Calculate the area of a Square.")
s=float(input("Enter Side:"))
area=s*s
print("Formula of Area of Rectangle= Side*Side")
print(f"The area of the Square is: {area}")
