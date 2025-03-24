import random

top_of_the_range = input("Type a Number: ")

if top_of_the_range.isdigit():
    top_of_the_range = int(top_of_the_range)
    if top_of_the_range<= 0:
        print("Please type in a larger number next time")
        quit()
else:
    print("Type in a number Next time mf")

random_nmber = random.randint(0, top_of_the_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Type in a number next time mf")
        continue
    
    
    if user_guess == random_nmber:
        print("you got it right ")
        break
    elif user_guess > random_nmber:
        print("You were above the number")

    else:
        print("You were below the number")
print("You got it in", guesses, "guesses")







