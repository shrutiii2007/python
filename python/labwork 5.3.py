# Q1
Set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print("Initial Set:", Set1)
Set1.add(11)
print("After adding 11:", Set1)
Set1.remove(1)
print("After removing 1:", Set1)
print()

# Q2
stud = {
    "Name": "shruti",
    "Age": 17,
    "City": "Monaco"
}
print("Initial Dictionary:", stud)
stud["Grno"] = 10311
print("After adding Grno:", stud)
stud["Age"] = 18
print("After updating Age:", stud)
stud.pop("Grno")
print("After removing Grno:", stud)
print()

# Q3
numbers_input = input("Enter numbers separated by spaces: ")  # e.g. 1 2 2 3 4
num_list = list(map(int, numbers_input.split()))
print("List:", num_list)
unique_numbers = set(num_list)
print("Unique numbers:", unique_numbers)
print()

# Q4
products = {'Laptop': 150000, 'Phone': 60000, 'BNWM4': 3000000}
print("Products:", products)
max_product = max(products, key=products.get)
print("Product with highest price:", max_product, "=", products[max_product])
print()

# Q5
list0 = [1, 2, 3, 4, 5]
tuple0 = (6, 7, 8, 9, 10)
set0 = {11, 12, 13, 14, 15}

print("Original list:", list0)
list_to_set = set(list0)
print("List converted to set:", list_to_set)
list_to_tuple = tuple(list0)
print("List converted to tuple:", list_to_tuple)
print()

print("Original tuple:", tuple0)
tuple_to_list = list(tuple0)
print("Tuple converted to list:", tuple_to_list)
print()

print("Original set:", set0)
set_to_list = list(set0)
print("Set converted to list:", set_to_list)
set_to_tuple = tuple(set0)
print("Set converted to tuple:", set_to_tuple)
print("Note: Sets remove duplicates and are unordered.")
print()

# Q6
user = input("Enter a string (comma-separated numbers): ")  # e.g. 1,2,3,4,4
user_list = user.split(",")
print("List from string:", user_list)
user_set = set(user_list)
print("Set from string:", user_set)
user_tuple = tuple(user_list)
print("Tuple from string:", user_tuple)
print()

# Q7
print("Q7: Set to dictionary with squares")
unique_integers = {1, 2, 3, 4}
square_dict = {num: num ** 2 for num in unique_integers}
print("Dictionary with squares:", square_dict)