
def factorial(n):
    if n == 1: 
        return 1
    if n < 0:             #galat input handle ki
        return "factorial doesn't take place in negative numbers"
    return n * factorial(n - 1)  

print(factorial(5))  
print(factorial(4))
print(factorial(-4))

# output is :- 120
# output is :- 24
# output is :- factorial doesn't take place in negative numbers
