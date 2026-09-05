import random
import string


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


if __name__ == "__main__":
    password_generator()