n = int(input("Enter array size: "))  
arr = []
print("Enter array elements:")
for i in range(n):
    arr.append(int(input(f"a[{i}] = "))) 

print("Length of the Array:",len(arr))

# output :-
# Enter array size: 4
# Enter array elements:
# a[0] = 1
# a[1] = 2
# a[2] = 3
# a[3] = 4
# Length of the Array: 4