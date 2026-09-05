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


if __name__ == "__main__":
    salary_finder()