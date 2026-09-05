import string
from collections import Counter


def character_counter():
    print("Welcome to Character counter made by Parth Agrawal")
    text = input("Enter your text: ").lower()
    counts = Counter(char for char in text if char.isalpha())

    for char in string.ascii_lowercase:
        print(f"The '{char}' occurs {counts[char]} times in your text")


if __name__ == "__main__":
    character_counter()