
value_1 = int(input("Enter the first number: "))
value_2 = int(input("Enter the second number: "))

condition = input("Enter an operator (+, -, *, /): ")

match condition:
        case '+':
            result = value_1 + value_2 
            print("answer is",result)
        case '-':
            result = value_1 - value_2 
            print("answer is",result)
        case '*':
            result = value_1 * value_2 
            print("answer is",result)
        case '/':
            result = value_1 / value_2 
            print("answer is",result)
        
# Enter the first number: 10
# Enter the second number: 20
# Enter an operator (+, -, *, /): +
# answer is 30

