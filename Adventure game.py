import random

def start_game():
    print("Welcome to the Adventure Game!")
    player_name = input("What is your name? ")
    print(f"Hello, {player_name}, Welcome to the Adventure!")
    first_choice()

def first_choice():
    print("\nYou are at a crossroad. Do you want to go Left or Right?")
    choice = input("Type 'left' or 'right': ").strip().lower()

    if choice == 'left':
        left_path()
    elif choice == 'right':
        right_path()
    else:
        print("Invalid choice! Please type 'Right' or 'Left'." )
        first_choice()

def left_path():
    print("\n You walked several miles and come to a river")
    print("Do you want to 'cross' the river or 'walk' along the river?")
    choice = input("Type 'Cross' or 'Walk': ").strip().lower()

    if choice == 'cross':
        print("You cross the river bu the water was too deep. You got swept away. You lost the game.")
    elif choice == 'walk':
        print("You walk along the river and find bridge. You can cross the bridge safely. You continue on your journey")
        second_left_decision()
    else:
        print("Invalid choice! Please type 'Cross' or 'Walk'.")
        left_path()

def second_left_decision():
    print("\n You find a treasure with a padlock.")
    print("Do you want to you want to 'Open' the chest or 'Leave' it?")
    choice = input("Type 'open' or 'leave': ").strip().lower()

    if choice == 'open':
        if random.randint(1,2) == 1:
            print("The chest opens and you find a bag Gold! You win!")
        else:
            print("It's a Trap! You got caught and lost the game.")
    elif choice == 'leave':
        print("You decide to leave the chest and continue on your journey.")
        # i will continue with more scenarios here
    else:
        print("Invalid choice! Please type 'open' or 'leave'.")
        second_left_decision()

def right_path():
    print("\n You walk several miles and you got to bridge.")
    print("Do you want to 'Cross' the bridge or 'Swim' across the bridge?")
    choice = input("Type 'sross' or 'swim': ").strip().lower()

    if choice ==  'cross':
        print("You cross the bridge safely and meet a stranger who gives you a gold coin. You continue on your adventure.")
        # i will add more point here later
    elif choice == 'swim':
        print("You tried to swim and got attacked by a crocodile. You lost the game.")
    else:
        print("Invalid choice! Please type 'Cross' or 'Swim'.")
        right_path()

start_game()