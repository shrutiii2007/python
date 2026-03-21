#1
row = 5
for i in range(1, row + 1):
    print("  " * (row - i), end="") 
    for j in range(i, 0, -1):        
        print(j, end=" ")
    print()
print("=============================================")

#2
row = 5
for i in range(row, 0, -1):              
    print("  " * (i - 1), end="")       
    for j in range(i, row + 1):          
        print(j, end=" ")
    print()
print("=============================================")

#3
row = 5
for i in range(row, 0, -1):              
    print("  " * (i - 1), end="")        
    for j in range(row - i + 1):          
        print(i, end=" ")                 
    print()
print("=============================================")

#4
rows = 5
for i in range(rows):
    print("  " * i, end="") 
    for j in range(rows - i):
        print((i + j) % 2, end=" ")
    print()

print("=============================================")

#5
rows = 5
for i in range(rows, 0, -1):
    print("  " * (rows - i), end="") 
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
print("=============================================")


#6
rows = 5
for i in range(0, rows):              
    print("  " * i, end="")            
    for j in range(rows, i, -1):       
        print(j, end=" ")
    print()
