def addition (a, b):
    return a + b 
def substract (a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide (a, b):
    return a / b
operations = {
    "+": addition,
    "-": substract,
    "*": multiply,
    "/": divide,
}
switch = "y"
first_num = int(input("Input the first number: "))
while switch == "y":
    for key in operations:
        print(key)
    operator = input("Pick an operation: ") 
    second_num = int(input("Input the next number: "))
    if operator == "+":
        output = operations[operator](first_num, second_num)
        print(f"{first_num} {operator} {second_num} = {output}")
    elif operator == "-":
        output = operations[operator](first_num, second_num)
        print(f"{first_num} {operator} {second_num} = {output}")
    elif operator == "*":
        output = operations[operator](first_num, second_num)
        print(f"{first_num} {operator} {second_num} = {output}")
    elif operator == "/":
        output = operations[operator](first_num, second_num)
        print(f"{first_num} {operator} {second_num} = {output}")
    first_num = output
    switch = input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation: ")
    
    