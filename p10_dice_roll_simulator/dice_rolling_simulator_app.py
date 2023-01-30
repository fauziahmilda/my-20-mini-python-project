import random
import os

# create the dictionary
dice_drawing = {
    1: (
        ".___________.",
        "|1          |",
        "|           |",
        "|     ♥️     |",
        "|           |",
        "|___________|",
    ),
    2: (
        ".___________.",
        "|2          |",
        "|   ♥️       |",
        "|           |",
        "|       ♥️   |",
        "|___________|",
    ),
    3: (
        ".___________.",
        "|3          |",
        "|   ♥️       |",
        "|     ♥️     |",
        "|       ♥️   |",
        "|___________|",
    ),
    4: (
        ".___________.",
        "|4          |",
        "|   ♥️   ♥️   |",
        "|           |",
        "|   ♥️   ♥️   |",
        "|___________|",
    ),
    5: (
        ".___________.",
        "|5          |",
        "|   ♥️   ♥️   |",
        "|     ♥️     |",
        "|   ♥️   ♥️   |",
        "|___________|",
    ),
    6: (
        ".___________.",
        "|6          |",
        "|   ♥️ ♥️ ♥️   |",
        "|           |",
        "|   ♥️ ♥️ ♥️   |",
        "|___________|",
    ),



}


# main function
def main():
    option = input("Roll the dice? (y/n) ")
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


# funtion to roll the dice
def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(f"dice rolled : {dice1} and {dice2}")
    print("\n".join(dice_drawing[dice1]))
    print("\n".join(dice_drawing[dice2]))
    main()


main()
