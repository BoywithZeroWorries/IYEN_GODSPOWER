import random

user_wins = 0
computer_wins = 0

options = ["Rock", "Paper", "Scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to Quit: " ).lower()     # Convert input to lower case
    if user_input == "q":
        break

    if user_input not in ["rock", "paper", "scissors"]:    # Check lowercase input
        print("Invalid choice, try again.")
        continue
   
    user_input = user_input.title()     # Convert to match list formatting ("Rock", "Paper", etc.)

    random_number = random.randint(0, 2)
    # Rock: 0, Paper: 1, Scissors: 2
    computer_pick = options[random_number]
    print(f"computer picked {computer_pick}.")

    if  (user_input == "Rock" and computer_pick == "Scissors") or \
        (user_input == "Paper" and computer_pick == "Rock") or \
        (user_input == "Scissors" and computer_pick == "Paper"):
        print("You won!")
        user_wins += 1
    elif user_input == computer_pick:
        print("it's a tie!")
    else:
        print("You lost!")
        computer_wins += 1
    
print(f"You won {user_wins} times.")
print(f"The computer won {computer_wins} times.")
print("Goodbye, Hoomie! ")