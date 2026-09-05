def acronym_generator():
    print("Welcome to the Acronym generator made by Parth Agrawal")
    text = input("Enter a text: ")
    words = text.split()
    if not words:
        print("No input provided.")
        return

    acronym = "".join(word[0] for word in words)
    print("Acronym:", acronym.upper())


if __name__ == "__main__":
    acronym_generator()