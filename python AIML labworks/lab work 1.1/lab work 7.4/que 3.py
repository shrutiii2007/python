size = int(input("Enter array size: "))

a = []
print("Enter array A's elements:")
for i in range(size):
    a.append(int(input(f"a[{i}] = ")))

b = []
print("Enter array B's elements:")
for i in range(size):
    b.append(int(input(f"b[{i}] = ")))

c = []
for i in range(size):
    c.append(a[i] + b[i])

print("Output:")
print("Array C is:", c)
