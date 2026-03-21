def check_even(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n % 2 != 0:
        raise ValueError("Number is odd")
    print("Number is even")

check_even(7)

# output:-
# Number is even                          if even then :-
# ValueError: Number is odd               if odd then :-