import random
import os

exit = False
user_points = 0
comp_points = 0

while exit == False:
    options = ["rock", "paper", "scissors"]

    user_input = input("Choose rock, paper, scissors, or exit: ")
    comp_input = random.choice(options)
    
    if user_input.lower() == "exit":
        os.system('cls')
        print(f"Your points: {user_points}")
        print(f"Comp points: {comp_points}")

        if user_points > comp_points:
            print("YOU WON this f*kn GAME")
        elif user_points == comp_points:
            print("DRAW !")
        elif user_points < comp_points:
            print("YOU LOOSE")
            
        print("\nBye")
        
        exit = True
        
    if user_input.lower() == "rock":
        if comp_input == "rock":
            print(f"Your input: {user_input}")
            print(f"Comp input: {comp_input}")
            print("SERI")
        elif comp_input == "paper":
            print(f"Your input: {user_input}")
            print(f"Comp input: {comp_input}")
            print("LOOSE")
            comp_points += 1
        elif comp_input == "scissors":
            print(f"Your input: {user_input}")
            print(f"Comp input: {comp_input}")
            print("WIN")
            user_points += 1
    if user_input.lower() == "paper":
        if comp_input == "rock":
            print(f"Your input: {user_input}")
            print(f"Comp input: {comp_input}")
            print("WIN")
            user_points += 1
        elif comp_input == "paper":
            print(f"Your input: {user_input}")
            print(f"Comp input: {comp_input}")
            print("SERI")
        elif comp_input == "scissors":
            print(f"Your input: {user_input}")
            print(f"Comp input: {comp_input}")
            print("LOOSE")
            comp_points += 1
    if user_input.lower() == "scissors":
        if comp_input == "rock":
            print(f"Your input: {user_input}")
            print(f"Comp input: {comp_input}")
            print("LOOSE")
            comp_points += 1
        elif comp_input == "paper":
            print(f"Your input: {user_input}")
            print(f"Comp input: {comp_input}")
            print("WIN")
            user_points += 1
        elif comp_input == "scissors":
            print(f"Your input: {user_input}")
            print(f"Comp input: {comp_input}")
            print("SERI")
    else:
        print("Invalid input !")        
            
