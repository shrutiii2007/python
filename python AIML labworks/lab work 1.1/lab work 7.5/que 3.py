matrix = [
    [1, 2, 3],  
    [4, 5, 6],  
    [7, 8, 9]  
]
print(matrix)

total_sum=0

for row in matrix:
    for coloumn in row:
        total_sum+=coloumn
print("sum of matrix:-",total_sum)

# output:-
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# sum of matrix:- 45