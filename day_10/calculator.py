def addition (a, b):
    return a + b 
def substract (a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide (a, b):
    return a / b
def operators():
    return ("+\n-\n*\n/")

switch = "y"
first_num = int(input("Input the first number: "))
while switch == "y":
    print(operators())
    operator = input("Pick an operation: ") 
    second_num = int(input("Input the next number: "))
    if operator == "+":
        output = addition(first_num, second_num)
        print(f"{first_num} {operator} {second_num} = {output}")
    elif operator == "-":
        output = substract(first_num, second_num)
        print(f"{first_num} {operator} {second_num} = {output}")
    elif operator == "*":
        output = multiply(first_num, second_num)
        print(f"{first_num} {operator} {second_num} = {output}")
    elif operator == "/":
        output = divide(first_num, second_num)
        print(f"{first_num} {operator} {second_num} = {output}")
    first_num = output
    switch = input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation: ")
    
    