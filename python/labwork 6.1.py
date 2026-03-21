#QUESTION 1

def list(numbers):

    print("List:", numbers)
    print("Length:", len(numbers))
    print("Maximum:", max(numbers))
    print("Sort(ascending):", sorted(numbers))
    print("Sum :", sum(numbers))
    print("Type:", type(numbers))

numbers = [12, 45, 23, 67, 89, 34, 22, 90, 11]
list(numbers)

#QUESTION 2

def number(num):
    print("Absolute value:", abs(num))
    print("Cube (num^3):", pow(num, 3))
    print("Rounded to 2 decimals:", round(num, 2))

num = float(input("Enter a negative float number: "))
number(num)

#QUESTION 3

def numbers():
  
    numbers = [23,45,87,98,56,32,19,76]
    
    print("List of numbers:", numbers)
    print("Minimum value:", min(numbers))
    print("Maximum value:", max(numbers))
    print("Sum of numbers:", sum(numbers))

numbers()

#QUESTION 4

def list():
    nums = [int(num) for num in input("enter numbers: ").split()]
    print("original list:", nums)

    print("ascending:", sorted(nums))

    print("descending:", sorted(nums, reverse=True))

    nums.reverse()
    print("reversed:", nums)

list()
