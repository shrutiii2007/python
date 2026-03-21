class InsufficientBalanceError(Exception):
    pass

balance = 3000

def withdraw(amount):
    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance")
    print("Withdrawal successful")


withdraw(5000)
# withdraw(2000)


# output:-
# Withdrawal successful                    3000 balance then withdrawal is 2000 then :-

# 3000 balance then withdrawal is 5000 then :-
# raise InsufficientBalanceError("Insufficient balance")