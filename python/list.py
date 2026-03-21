# Q1
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(f"Hello, {last_name}. {first_name}!")
print()


# Q2
item = "apple"
price = 5.50
print(f"The price of  {item} is {price} dollars.")
print()

# Q3

string = input("Enter a string: ")
reversed_str = string[::-1]
print("Reversed string:", reversed_str)
if string.lower() == reversed_str.lower():
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")


#Q4
text = input("Enter a string: ")
print( text.upper())
print( text.lower())
print( text.title())



#Q5
names = ["nij", "ashu", "meet", "darshil", "parth"]
print("Total number of names:", len(names))