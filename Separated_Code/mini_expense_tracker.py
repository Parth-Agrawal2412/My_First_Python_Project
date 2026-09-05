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


if __name__ == "__main__":
    mini_expense_tracker()