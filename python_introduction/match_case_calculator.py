num1 = int(input("Enter the first number:" ))
num2 = int(input("Enter the second number:" ))


operation = input("Choose an operation (add, subtract, multiply, divide): ")
operation = operation.lower()
match operation:
    case "add":
        result = num1 + num2
        print(f"The result of adding {num1} and {num2} is {result}.")
    case "subtract":
        result = num1 - num2
        print(f"The result of subtracting {num2} from {num1} is {result}.")
    case "multiply":
        result = num1 * num2
        print(f"The result of multiplying {num1} and {num2} is {result}.")
    case "divide":
        if num2 != 0:
            result = num1 / num2
            print(f"The result of dividing {num1} by {num2} is {result}.")
        else:
            print("Error: Division by zero is not allowed.")    
    case _:
        print("Invalid operation selected.")
    
