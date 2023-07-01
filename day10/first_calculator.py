#Calculator


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
operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

num1 = int(input("What's the first number? "))
num2 = int(input("What's the second number? "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from the line above: ")
calculation_function = operations[operation_symbol]  #important sentence
# calculation_function = operations["*"] = multiply
answer = calculation_function(num1, num2)  #add(n1, n2) / divide(n1, n2)

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

print(f"{num1} {operation_symbol} {num2} = {answer}")
