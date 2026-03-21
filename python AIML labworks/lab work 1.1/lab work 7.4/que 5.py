arr = [int(x) for x in input("Enter elements: ").split()]
target = int(input("Search: "))

if target in arr:
    print("Found at index")
else:
    print("Not Found")
