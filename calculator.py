
def calculator():
    print("Welcome to My Python Calculator!")

    first = float(input("Enter the first number: "))
    operator = input("Choose an operator (+, -, *, /): ")
    second = float(input("Enter the second number: "))

    if operator == "+":
        result = first + second
    elif operator == "-":
        result = first - second
    elif operator == "*":
        result = first * second
    elif operator == "/":
        if second == 0:
            print("Error: Cannot divide by zero.")
            return
        result = first / second
    else:
        print("Invalid operator.")
        return

    print("Result:", result)


if __name__ == "__main__":
    calculator()
