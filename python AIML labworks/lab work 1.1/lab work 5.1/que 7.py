   #Q7

text = "Hello everyone, Welcome to the World"
print("Starts with Hello?", text.startswith("Hello"))
print("Ends with World?", text.endswith("World"))


data = "Data123#Science!"
cleaned = "".join(ch for ch in data if ch.isalpha())
print("Cleaned string:", cleaned)

word = "Python"
print("Reversed:", word[::-1])