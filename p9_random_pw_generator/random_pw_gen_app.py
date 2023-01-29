# ask the user want to generate the password or not
# if yes ask for password
# generate the password
# print password

import string
import random
import os

# create list, amount char that we want to generate
character = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def main():
    option = input("Do you want to generate the password? (y/n) ")
    if option.lower() == "y":
        generate_pw()
    elif option.lower() == "n":
        os.system('cls')
        print("Bye")
        exit()

    else:
        os.system('cls')
        print("Error, please try again.")
        print("")
        main()


def generate_pw():
    os.system('cls')
    password_length = int(
        input("How long would you like your password to be? "))

    random.shuffle(character)  # first shuffle

    # create password as empty list
    password = []

    for x in range(password_length):
        password.append(random.choice(character))

    random.shuffle(password)  # shuffle again to make it more random

    # convert that list to be string
    password = "".join(password)

    print(f"Your password: {password}")
    print("")
    main()


main()
