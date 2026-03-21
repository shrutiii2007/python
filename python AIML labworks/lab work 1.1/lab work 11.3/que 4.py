def check_palindrome(s):
    assert s != "", "Input string cannot be empty"

    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")

check_palindrome("shruti")

# output:-

# Palindrome                    if name is level or kanak and many more than answer is :-
# Not a palindrome              if name is like shruti or laptop or many more than answer is :-