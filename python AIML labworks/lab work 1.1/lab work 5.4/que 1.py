students = [
    {"id": 101, "name": "Alice", "score": 85},
    {"id": 102, "name": "Bob", "score": 78},
    {"id": 103, "name": "Charlie", "score": 92}
]

#que 1
print("Student Names:")
for student in students:
    print(student["name"])
#output
# Student Names:
# Alice
# Bob
# Charlie

#QUE 2 
total = 0
for student in students:
    total += student["score"]
avg = total / len(students)
print("\nAverage Score:", avg)

#QUE 3
students.append({"id": 104, "name": "rahul", "score": 88})
print()
print("Added New Student: rahul")
print(students)
# output:-
# Added New Student: rahul
# [{'id': 101, 'name': 'Alice', 'score': 85}, {'id': 102, 'name': 'Bob', 'score': 78},
#   {'id': 103, 'name': 'Charlie', 'score': 92}, {'id': 104, 'name': 'rahul', 'score': 88}]

#QUE 4
students[1].update({"score": 88})
print()
print("Updated Students List:")
print(students)
# output:-
# Updated Students List:
# [{'id': 101, 'name': 'Alice', 'score': 85}, {'id': 102, 'name': 'Bob', 'score': 88},
# {'id': 103, 'name': 'Charlie', 'score': 92}, {'id': 104, 'name': 'rahul', 'score': 88}]

#QUE 5
print("removing charlie")
students.remove({'id': 103, 'name': 'Charlie', 'score': 92})
print(students)
print()
# output:-
# [{'id': 101, 'name': 'Alice', 'score': 85}, 
# {'id': 102, 'name': 'Bob', 'score': 88}, 
# {'id': 104, 'name': 'rahul', 'score': 88}]

#QUE 6
print("Students who scored more than 80:")
for student in students:
  if student["score"] > 80:
   print(student["name"])
print()
#output
# Students who scored more than 80:
# Alice
# Bob
# rahul

#QUE 7
for i in range(len(students)):
   for j in range(i+1,len(students)):
      if students[i]["score"] < students[j]["score"]:
         students[i],students[j] = students[j],students[i]
print("studnets sorted by score :-")
for student in students:
   print(student)
# #output:-
# #studnets sorted by score :-
# {'id': 102, 'name': 'Bob', 'score': 88}
# {'id': 104, 'name': 'rahul', 'score': 88}
# {'id': 101, 'name': 'Alice', 'score': 85}

# QUE 8
print()
highest = students[0]
for student in students:
   if student["score"] > highest["score"]:
      highest = student
print("highest score:-")
print(highest)
# output:-
# highest score:-
# {'id': 102, 'name': 'Bob', 'score': 88}
