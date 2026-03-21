matrix = [
    [1, 2, 3],  
    [4, 5, 6] 
]
print("original matrix :-",matrix)
print("transposed matrix:-")
for col in range(len(matrix[0])):  
    for row in matrix:
        print(row[col], end=" ")
    print()

# output:-
# original matrix :- [[1, 2, 3], [4, 5, 6]]
# transposed matrix:-
# 1 4
# 2 5
# 3 6