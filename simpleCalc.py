operand1 = 0
operand2 = 0
result = 0
operator = ""
got_operand1 = False
got_operand2 = False
got_result = False

while got_operand1 == False:
    operand1 = input("Enter your first number: ")
    try:
        operand1 = float(operand1)
    except ValueError:
        print("Enter a number")
    if type(operand1) == float:
        got_operand1 = True

while got_operand2 == False:
    operand2 = input("Enter your second number: ")
    try:
        operand2 = float(operand2)
    except ValueError:
        print("Enter a number")
    if type(operand2) == float:
        got_operand2 = True

while got_result == False:
    operator = input("Enter an operator (+ - * /): ")
    if operator == "+":
        result = operand1 + operand2
        got_result = True
    elif operator == "-":
        result = operand1 - operand2
        got_result = True
    elif operator == "*":
        result = operand1 * operand2
        got_result = True
    elif operator == "/":
        if operand2 != 0:
            result = operand1 / operand2
            got_result = True
        else:
            print("Cannot divide by zero! Select a different operator")   

print(str(operand1)+" "+str(operator)+" "+str(operand2)+" = "+str(result))
