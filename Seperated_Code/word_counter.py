def word_counter():
    print("Welcome to the Word counter made by Parth Agrawal")
    text = input("Enter your text: ")
    words = text.split()
    print("Total words:", len(words))


if __name__ == "__main__":
    word_counter()