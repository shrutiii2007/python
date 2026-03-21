students = [
    {"name": "ratnesh", "age": 45},
    {"name": "babita", "age": 44},
    {"name": "shruti", "age": 18}
]

sorted_students = sorted(students, key=lambda x: x["age"])
print(sorted_students)


# output:-

# [{'name': 'shruti', 'age': 18},
#  {'name': 'babita', 'age': 44}, 
# {'name': 'ratnesh', 'age': 45}]

