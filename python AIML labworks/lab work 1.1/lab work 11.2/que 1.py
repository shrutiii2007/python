try:
    a=int(input("enter first number:-"))
    b=int(input("enter second number:-"))
    result=a/b
    print("result",result)
except ZeroDivisionError:
    print("Error :- Division by zero is not allowed.")


# output:-

# enter first number:-10
# enter second number:-0
# Error :- Division by zero is not allowed.

# enter first number:-10
# enter second number:-2
# result 5.0