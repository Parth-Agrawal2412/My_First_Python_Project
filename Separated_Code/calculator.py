def calculator():
    print("Welcome to the Calculator made by Parth Agrawal")
    equation = input("Enter your Equation (e.g., 10 + 5): ")
    split_equation = equation.split()

    if len(split_equation) != 3:
        print("Invalid input format. Please format as: number operator number")
        return

    try:
        num1 = float(split_equation[0])
        operator = split_equation[1]
        num2 = float(split_equation[2])
    except ValueError:
        print("Error: Please enter valid numbers.")
        return

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print("Invalid operator! Use +, -, *, or /.")
        return

    print("Your result was:", result)


if __name__ == "__main__":
    calculator()