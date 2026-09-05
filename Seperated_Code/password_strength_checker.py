import string


def password_strength_checker():
    print("Welcome to the Password strength checker made by Parth Agrawal")
    password = input("Enter your password: ")
    password_strength = 0

    if len(password) >= 8:
        password_strength += 5 + (len(password) - 8)

    if any(char.isdigit() for char in password):
        password_strength += 5
    if any(char.isupper() for char in password):
        password_strength += 5
    if any(char in string.punctuation for char in password):
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


if __name__ == "__main__":
    password_strength_checker()