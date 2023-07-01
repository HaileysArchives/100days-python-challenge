import calculator_art #from calculator_art import logo
#Calculator

print(calculator_art.logo)

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

#Create a dictionary named operations
operations = {
    "+",
    "-",
    "*",
    "/"
}

def calculator():
    num1 = float(input("What's the first number? "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operations: ")
        num2 = float(input("What's the next number? "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else: 
            should_continue = False
            calculator()


# num1 = int(input("Whats the first number? "))
# num2 = int(input("What's the next number? "))

# for symbol in operations:
#     print(symbol)

# operation_symbol = input("Pick an operation from the line above: ")
# calculation_function = operations[operation_symbol] # important sentence => calculation_function = operations["*"] = multiply
# ask_continue = input("Type 'y' to continue calculating with 8, or type 'n' to exit.: ")
# answer = calculation_function(num1, num2) # add(n1, n2), divide(n1, n2)

# end_Calculator = (ask_continue == "y")
# while end_Calculator:
#     num2 = int(input("What's the next number? "))
#     operation_symbol = input("Pick an operation from the line above: ")
#     answer = calculation_function(num2, num2)

#     calculation_function = operations[operation_symbol]
#     if ask_continue == "n":

# print(f"{num2} {operation_symbol} {num2} = {answer}")

        
#my calculator code

# def calculator(symbol):
#     n1 = num1
#     n2 = num2
#     symbol = operation_symbol
    
#     if symbol == "+":
#         add(n1, n2)
#     elif symbol == "-":
#         subtract(n1, n2)
#     elif symbol == "*":
#         multiply(n1, n2)
#     elif symbol == "/":
#         divide(n1, n2)

# answer = calculator()