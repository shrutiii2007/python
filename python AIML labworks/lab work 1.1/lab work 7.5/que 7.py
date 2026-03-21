list_dicts = [
    {'name': 'Alice', 'age': 33},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 32},
    {'name': 'David', 'age': 25}
]

sorted_age = sorted(list_dicts, key=lambda item: item['age'])

print(sorted_age)
