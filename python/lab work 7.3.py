#QUESTION 1

arr = [12, 45, 2, 67, 33, 89, 23]

max_val = arr[0]
min_val = arr[0]
max_index = 0
min_index = 0

for i in range(len(arr)):
    if arr[i] > max_val:
        max_val = arr[i]
        max_index = i
    if arr[i] < min_val:
        min_val = arr[i]
        min_index = i

print("Q1: Max value is", max_val, "at index", max_index)
print("Q1: Min value is", min_val, "at index", min_index)


#QUESTION 2

cumulative = []
s = 0
for x in arr:
    s = s + x
    cumulative.append(s)

print(" Cumulative Sum:", cumulative)


#QUESTION 3

unique = []
for x in arr:
    if x not in unique:
        unique.append(x)

print(" Unique elements and frequency:")
for u in unique:
    count = 0
    for x in arr:
        if x == u:
            count += 1
    print(u, "occurs", count, "times")


#QUESTION 4

div_by_3 = []
for x in arr:
    if x % 3 == 0:
        div_by_3.append(x)

print(" No. divisible by 3:", div_by_3)


#QUESTION 5

N = int(input("Enter N for Fibonacci: "))
fib = []
a, b = 0, 1

for i in range(N):
    fib.append(a)
    a, b = b, a+b

print(" First", N, "Fibonacci numbers:", fib)
