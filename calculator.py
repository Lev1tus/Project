def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
math = "y"
while math == "y":
    variables = "incorrect"
    while variables == "incorrect":
        try:
            variables = "correct"
            x = int(input("What's x? "))
            y = int(input("What's y? "))
        except ValueError:
            variables = "incorrect"
            print("x and y are not integers. Try again.")
    op = input("What do you want to do with x and y? add/subtract/multiply/divide ")
    if op == "add":
        print(add(x, y))
    elif op == "subtract":
        print(subtract)
    elif op == "multiply":
        print(multiply(x, y))
    elif op == "divide":
        print(divide(x, y))
    
    math = str(input("Do you want to do math again? y/n "))
    