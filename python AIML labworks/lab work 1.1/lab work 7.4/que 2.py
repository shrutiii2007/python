n = int(input("Enter array size: "))  
arr = []
print("Enter array elements:")
for i in range(n):
    arr.append(int(input(f"a[{i}] = "))) 

print("Length of the Array:", len(arr))

if n > 0:
    average = sum(arr) / n
    print("Average of the array:", average)
else:
    print("Cannot compute average of an empty array.")
