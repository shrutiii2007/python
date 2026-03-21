student = {"name": "alice", "age": 20, "grade": "A"}

print(student.keys())    
print(student.values())   

student.pop("grade")   
print(student)             

student["age"] = 21

student.update({"city": "delhi"})

print(student)

# output is :

# dict_keys(['name', 'age', 'grade'])
# dict_values(['alice', 20, 'A'])
# {'name': 'alice', 'age': 20}
# {'name': 'alice', 'age': 21, 'city': 'delhi'}

# #Create a dictionary:
# student = {"name": "Alice", "age": 20, "grade": "A"}

# Print the keys and values
# Add a new key: "city": "Delhi"
# Update "age" to 21
# Delete the "grade" key

