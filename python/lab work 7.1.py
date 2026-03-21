#QUESTION 1

arr = [10, 20, 30, 40, 50]

print("Array elements:")
for num in arr:
    print(num)

#QUESTION 2

arr = [5, 10, 15, 20, 25]

total = 0
for num in arr:
    total += num

print("Sum of array elements:", total)

#QUESTION 3

arr = [12, 45, 2, 67, 34]

print("Maximum:", max(arr))
print("Minimum:", min(arr))

#QUESTION 4

arr = [1, 2, 3, 4, 5]

arr.insert(2, 99)

print("Array after inserting:", arr)

#QUESTION 5

arr = [10, 20, 30, 40, 50]

arr.remove(30)

print("Array after deletion:", arr)

#QUESTION 6

arr = [100, 200, 300, 400]

arr[2] = 999

print("Updated array:", arr)

#QUESTION 7

arr = [10, 20, 30, 40, 50]

a = 40
if a in arr:
    print("Element found at index:", arr.index(a))
else:
    print("Element not found")

#QUESTION 8

a = [1, 2, 3]
b = [4, 5, 6]

c = a + b
print("Concatenated array:", c)

#QUESTION 9

arr = [50, 20, 40, 10, 30]

arr.sort()
print("Sorted array:", arr)
