num = input("Enter Number:") 

a = bool(int(num)) 
print(type(a))

b = int(a) 
print("Your number in integer:", b)
print(type(b))

c = str(a) 
print("Your number in String:", c)
print(type(c))

# output:-
# Enter Number:5
# <class 'bool'>
# Your number in integer: 1
# <class 'int'>
# Your number in String: True
# <class 'str'>