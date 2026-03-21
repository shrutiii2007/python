def factorial(n):
    if n == 0 or n == 1:
        return 1  
    else:
        return n * factorial(n - 1)  
    
n = int(input("enter any num :-"))
result = factorial(n)
print("answers is :", result)

# output:-
# enter any num :- 5
# answers is : 120