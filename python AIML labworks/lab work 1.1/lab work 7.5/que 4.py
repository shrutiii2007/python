matrix = [
    [12, 32, 63],  
    [40, 55, 16],  
    [73, 89, 91]  
]
print(matrix)
max_value=matrix[0][0]  #start 12
min_value=matrix[0][0]
for row in matrix:                   #Row milti hai ek-ek karke:
    for coloumn in row:              #Isse har row ka har number milega.
        if coloumn > max_value:
            max_value = coloumn
        if coloumn < min_value:
            min_value = coloumn

print("Max value :", max_value)
print("Min value :", min_value)

# output:-
# [[12, 32, 63], [40, 55, 16], [73, 89, 91]]
# Max value : 91
# Min value : 12