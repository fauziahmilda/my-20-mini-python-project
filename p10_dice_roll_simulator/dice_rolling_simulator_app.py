import os


def main():
    option = input("Roll again? (y/n) ")
    if option.lower() == "y":
        os.system('cls')
        roll_dice()
    elif option.lower() == "n":
        os.system('cls')
        print("Bye")
        quit()
    else:
        os.system('cls')
        print("Error. Please try again! \n")
        main()


def roll_dice():
    pass
