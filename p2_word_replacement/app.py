# replace method in python

def replace_word():
    str = input("Enter random quote: ")
    print("-------------------------------")
    print(f"This is your quote: {str}")

    word_to_replace = input("Enter the word to replace: ")
    word_replacement = input("Enter the word replacement: ")
    print("After replacement: ", str.replace(
        word_to_replace, word_replacement))


replace_word()
