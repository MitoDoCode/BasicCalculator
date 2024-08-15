print("  >unDDLC Calculator<  ")

def OperatorTobeUsed(fnum, snum, ope):
    match ope:
        case "x":
            return fnum * snum, 0
        case "/":
            if snum == 0:
                return "Monika: Division by zero is not allowed Dummy.", 1
            return fnum / snum, 0
        case "+":
            return fnum + snum, 0
        case "-":
            return fnum - snum, 0
        case _:
            return "Monika: Invalid Operator.", 1

def GetNumInput(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Monika: Enter a valid number.")

def GetOpeInput(prompt):
    while True:
        operator = input(prompt).strip()
        if operator in {"x", "/", "+", "-"}:
            return operator
        print("Monika: Enter one of the following: x, /, +, -")

while True:
    Number1 = GetNumInput("Monika: First Number> ")
    operator = GetOpeInput("Monika: Enter Operator (x, /, +, -)> ")
    Number2 = GetNumInput("Monika: Second Number> ")

    result, Invalid = OperatorTobeUsed(Number1, Number2, operator)

    if Invalid == 0:
        print(f"Monika: The result of {Number1} {operator} {Number2} is {result}.")
    else:
        print(result)
