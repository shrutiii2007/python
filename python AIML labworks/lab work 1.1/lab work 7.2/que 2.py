# formula of fib :- fob(n)=fib(n-1) + fib(n-2)

def fibonacci(n):
    if n<0:
        return "invalid input"
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))