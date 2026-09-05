import random
import string
from collections import Counter


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


def acronym_generator():
    print("Welcome to the Acronym generator made by Parth Agrawal")
    text = input("Enter a text: ")
    words = text.split()
    if not words:
        print("No input provided.")
        return

    acronym = "".join([i[0] for i in words])
    print("Acronym:", acronym.upper())


def bill_generator():
    print("Welcome to the Bill generator made by Parth Agrawal")
    try:
        item_value = int(input("Enter how many Items do you want to add in your bill: "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

    items, unit_prices, quantities, costs = [], [], [], []

    for i in range(item_value):
        try:
            input_item = input(f"Enter your item name: ")
            input_cost = float(input(f"Enter cost of {input_item}: "))
            input_quantity = int(input(f"Enter the quantity of {input_item}: "))
        except ValueError:
            print("Invalid input type entered. Skipping remaining inputs.")
            return

        items.append(input_item)
        unit_prices.append(input_cost)
        quantities.append(input_quantity)
        costs.append(input_cost * input_quantity)

    total_amount = sum(costs)
    total_items = sum(quantities)

    try:
        discount = float(input("Enter discount in percentage(%), if none enter 0: "))
    except ValueError:
        discount = 0.0

    total_discount = (total_amount * discount) / 100
    final_amount = total_amount - total_discount

    print(f"The total amount to be paid is {final_amount:.2f}")
    choice = input("Do you want to print bill (y / n): ")
    if choice.lower() == "y":
        print("\n" + "-" * 55)
        print(f"{'S.No':<5} {'Item Name':<20} {'Price':<10} {'Qty':<8} {'Total':<10}")
        print("-" * 55)

        for i in range(len(items)):
            print(f"{i+1:<5} {items[i]:<20} {unit_prices[i]:<10.2f} {quantities[i]:<8} {costs[i]:<10.2f}")

        print("-" * 55)
        print(f"Total Amount: {total_amount:.2f}")
        print(f"Total Items:  {total_items}")
        print(f"Discount:     {total_discount:.2f}")
        print(f"Final Amount: {final_amount:.2f}")
        print("-" * 55)


def mini_expense_tracker():
    print("Welcome to Mini expense tracker made by Parth Agrawal")
    items, costs = [], []
    try:
        times = int(input("Enter how many items you have: "))
        for _ in range(times):
            choice = input("Enter your item name: ")
            choice_cost = float(input("Enter the cost of the item: "))
            items.append(choice)
            costs.append(choice_cost)
    except ValueError:
        print("Invalid number input.")
        return

    daily_wage_input = input("Enter your Daily Wage (type 'not sure' to find daily wage by monthly income): ").lower()

    if "not sure" in daily_wage_input:
        try:
            monthly_income = float(input("Enter your monthly income: "))
            days_worked = int(input("Enter how many days you work in a month: "))
            daily_wage = monthly_income / days_worked
            print(f"Your calculated daily wage is {daily_wage:.2f}")
        except (ValueError, ZeroDivisionError):
            print("Invalid inputs for daily wage calculation.")
            return
    else:
        try:
            daily_wage = float(daily_wage_input)
        except ValueError:
            print("Invalid wage entered.")
            return

    total_expense = sum(costs)
    money_saved = daily_wage - total_expense
    print(f"Your total expense is {total_expense:.2f} and money saved is {money_saved:.2f}")


def password_generator():
    print("Welcome to the Password generator made by Parth Agrawal")
    try:
        password_len = int(input("Enter your desired password length: "))
    except ValueError:
        print("Please enter a valid length.")
        return

    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(all_chars) for _ in range(password_len))
    print("Your new password is:", password)


def password_strength_checker():
    print("Welcome to the Password strength checker made by Parth Agrawal")
    password = input("Enter your password: ")
    password_strength = 0

    if len(password) >= 8:
        password_strength += 5 + (len(password) - 8)

    has_number = any(char.isdigit() for char in password)
    has_uppercase = any(char.isupper() for char in password)
    has_special = any(char in string.punctuation for char in password)

    if has_number:
        password_strength += 5
    if has_uppercase:
        password_strength += 5
    if has_special:
        password_strength += 5

    print(f"Your Password Strength points is {password_strength}")
    if password_strength == 0:
        print("Rating: Extremely Weak password")
    elif password_strength < 5:
        print("Rating: Very Weak password")
    elif password_strength <= 10:
        print("Rating: Weak password")
    elif password_strength <= 15:
        print("Rating: Good password")
    elif password_strength <= 20:
        print("Rating: Strong password")
    elif password_strength <= 25:
        print("Rating: Very Strong password")
    else:
        print("Rating: Extremely Strong password")


def character_counter():
    print("Welcome to Character counter made by Parth Agrawal")
    text = input("Enter your text: ").lower()
    counts = Counter(c for c in text if c.isalpha())

    for char in string.ascii_lowercase:
        print(f"The '{char}' occurs {counts[char]} times in your text")


def word_counter():
    print("Welcome to the Word counter made by Parth Agrawal")
    text = input("Enter your text: ")
    words = text.split()
    print("Total words:", len(words))


def salary_finder():
    print("Welcome to my Salary finder")

    while True:
        print("\nChoose input type:\n 1. Daily wage\n 2. Monthly Salary\n 3. Yearly salary")
        salary_choice_input = input("Enter Choice (1, 2, 3) or 'stop' to exit: ")

        if salary_choice_input.lower() == "stop":
            break

        if salary_choice_input not in ["1", "2", "3"]:
            print("Enter a valid choice (1, 2, or 3)!")
            continue

        try:
            salary_input = float(input("Enter Salary Amount: "))
        except ValueError:
            print("Please enter a valid numeric salary.")
            continue

        print("\nChoose target unit:\n 1. Daily wage\n 2. Monthly Salary\n 3. Yearly salary")
        salary_convert_input = input("Enter Choice (1, 2, 3): ")

        final_salary = 0.0
        if salary_choice_input == "1" and salary_convert_input == "2":
            final_salary = salary_input * 30
        elif salary_choice_input == "1" and salary_convert_input == "3":
            final_salary = salary_input * 365
        elif salary_choice_input == "2" and salary_convert_input == "1":
            final_salary = salary_input / 30
        elif salary_choice_input == "2" and salary_convert_input == "3":
            final_salary = salary_input * 12
        elif salary_choice_input == "3" and salary_convert_input == "2":
            final_salary = salary_input / 12
        elif salary_choice_input == "3" and salary_convert_input == "1":
            final_salary = salary_input / 365
        elif salary_choice_input == salary_convert_input:
            final_salary = salary_input
        else:
            print("Invalid target conversion option!")
            continue

        print(f"Your converted salary is: {final_salary:.2f}")


print("Welcome to the Ultimate program made by Parth Agrawal")
while True:
    choice2 = input("\nWant to run program (y or n): ").lower()
    if choice2 == "y":
        print("""
        1. Calculator
        2. Acronym Generator
        3. Bill Generator
        4. Mini Expense Tracker
        5. Password Generator
        6. Password Strength Checker
        7. Character Counter
        8. Word Counter
        9. Salary Finder
        """)
        choice = input("Enter your choice (1 to 9 or 'stop' to exit): ").lower()
        if choice == "stop":
            break
        elif choice == "1":
            calculator()
        elif choice == "2":
            acronym_generator()
        elif choice == "3":
            bill_generator()
        elif choice == "4":
            mini_expense_tracker()
        elif choice == "5":
            password_generator()
        elif choice == "6":
            password_strength_checker()
        elif choice == "7":
            character_counter()
        elif choice == "8":
            word_counter()
        elif choice == "9":
            salary_finder()
        else:
            print("Invalid choice, please try again.")
    else:
        break