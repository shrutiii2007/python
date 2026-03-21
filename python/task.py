#1
list = [2,8,9,2,4,5,3,6]
even, odd =[],[]
for i in list:
    if i %2==0:
        even.append(i)
    else:
        odd.append(i)
print(odd)
print(even)



#2
even=0
odd=0
for i in list:
    if i %2==0:
        even+=i
    else:
        odd+=i
print(even)
print(odd)




#3
Largest=max(list)
smallest=min(list)
print(Largest)
print(smallest)



#4
total_sum = sum(list)
print( total_sum)




#5
l1=[2,5,3,8,6,9]
lenght=len(l1)
for i in range (lenght):
    for j in range (0,lenght-1):
        if l1[j]>l1[j+1]:
            tmp=l1[j]
            l1[j]=l1[j+1]
            l1[j+1]=tmp



#6
lst2 = [1, 2, 3, 2, 1]
if lst2 == lst2[::-1]:
    print("List is palindrome")
else:
    print("List is not palindrome")


#7
    tuple = tuple(set(list))
print( tuple)




#8
list[0], list[-1] = list[-1], list[0]
print( list)



#9
list= list[::-1]
print( list)



#10
for i in range(len(list)):
    for j in range(i+1, len(list)):
        if list[i] > list[j]:
            list[i], list[j] = list[j], list[i]
print( list)