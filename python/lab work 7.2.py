#QUESTION 1

n = int(input("Enter array size: "))
a = []

print("Enter array elements:")
for i in range(n):
    val = int(input("a[" + str(i) + "] = "))
    a.append(val)

count = 0
for x in a:
    count = count + 1

print("Length of an Array:", count)

#QUESTION 2

n = int(input("Enter array size: "))

a = []
print("Enter array elements:")
for i in range(n):
    val = int(input("a[" + str(i) + "] = "))
    a.append(val)

sum = 0
for i in range(n):
    sum = sum + a[i]

avg = sum / n

print("Average of an Array:", avg)

#QUESTION 3

size = int(input("Enter array size: "))

a = []
b = []
c = []

print("\nEnter array A's elements:")
for i in range(size):
    num = int(input(f"a[{i}] = "))
    a.append(num)

print("\nEnter array B's elements:")
for i in range(size):
    num = int(input(f"b[{i}] = "))
    b.append(num)

for i in range(size):
    c.append(a[i] + b[i])

print("\nOutput:")
print("Array C is:", end=" ")
for num in c:
    print(num, end=", ")

#QUESTION 4

a = []

for i in range(1, 11):
    a.append(i)

print("Original Array:", a)

print("Array after multiplying each element by 2:")
for i in range(len(a)):
    a[i] = a[i] * 2
    print(a[i], end=" ")

#QUESTION 5

a = [10, 20, 30, 40, 50]

num = int(input("Enter a number to search: "))

found = False
for i in range(len(a)):
    if a[i] == num:
        print("Number found at index:", i)
        found = True
        break

if not found:
    print("Not Found")

#QUESTION 6

n = int(input("Enter size of array: "))

a = []
print("Enter array elements:")
for i in range(n):
    val = int(input("a[" + str(i) + "] = "))
    a.append(val)

print("Even numbers in array:")
for i in range(n):
    if a[i] % 2 == 0:
        print(a[i], end=" ")

print("\nOdd numbers in array:")
for i in range(n):
    if a[i] % 2 != 0:
        print(a[i], end=" ")

#QUESTION 7

n = int(input("Enter size of array: "))

a = []
print("Enter array elements:")
for i in range(n):
    val = int(input("a[" + str(i) + "] = "))
    a.append(val)

print("First five elements of array:")
for i in range(5):
    if i < n:
        print(a[i], end=" ")

print("\nAlternate elements of array:")
for i in range(0, n, 2):
    print(a[i], end=" ")

#QUESTION 8

n = int(input("Enter size of array: "))

a = []
print("Enter array elements:")
for i in range(n):
    val = int(input("a[" + str(i) + "] = "))
    a.append(val)

if n > 0:
    print("First element:", a[0])
    print("Last element:", a[n-1])
    middle_index = n // 2
    print("Middle element:", a[middle_index])
else:
    print("Array is empty")
