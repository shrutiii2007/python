#question 1

name = input("enter your name:")
print(type(name),name)
age = input ("enter your age:")
print (type(age),age)
height = input("enter your height:")
print(type(height),height)
verify = (input("info is True/False:"))
print (type(verify),verify)


print("type casting construction")

print()

#type construction

name = str(name)
print(name)
print(type(name))

age = int(age)
print(age)
print(type(age))

height = float(height)
print(height)
print(type(height))

verify = bool(verify)
print(verify)
print(type(verify))
