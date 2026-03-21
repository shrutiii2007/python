a=[1,2,3,4,5,6,7,8,9,10]
a.append(11)
print("Update list:",a)
print()



#2
user_list=input("Enter a number list: ")
large=max(user_list)
small=min(user_list)
print("Largest number:", large)
print("Smallest number:", small)

print()



#3
tuple_list =(1,2,2,3,4,4,5)
duplicate_list = tuple(set(tuple_list))
print(duplicate_list)
print()
list=list(tuple_list)
append_list = list.append(6)
print(list)



#4
b=[1,2,3,4,5]
b[2]=10
print (b)
print()



#5
nested_list = [1,[2,3],4,5]
print("nested list:",nested_list)
nested_list[1][0] = 20
nested_list[1][1] = 30
print("Updated nested list:", nested_list)
print()



#6
my_list = [1, 2, 3, 4, 5]
my_list.insert(2, 10)
my_list.remove(4)
my_list[0] = 20
print("Updated list:", my_list)
print()



#7
my_list2 = ([1,2], [3,4], [5,6])
my_list2[1][0] = 10
my_list2[1][1] = 20
print("Updated nested list:", my_list2)
print()



#8
a=10
b=20
c=b
b=a
a=c
print("a:", a)
print("b:", b)



#9
a=10
b=20-a
a=a+b
print("a:", a)
print("b:", b)