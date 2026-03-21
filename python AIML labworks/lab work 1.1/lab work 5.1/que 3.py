# Q3
text=input("Enter your name:")
reversed_text=text[::-1]
print("Reversed name",reversed_text)

if(text == reversed_text):
    print("Name is Palindrome ")
else:
    print("Name is not palindrome")