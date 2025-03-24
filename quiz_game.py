# Welcome to my mini quiz game!!

print("Welcome to my computer quiz")

playing = input("Do you want to play? ")
if playing != "yes":
    quit()
print("Okay! Let's Play..... ")
score = 0

answer = input("What does CPU stand For? ")
if answer == 'Central processing unit' :
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Youtube is owned by who? ")
if answer == "Google":
    print('Corect!')
    score += 1
else:
    print('Incorrect!')

answer = input("What color is the sky? ")
if answer == 'Blue':
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Who is the founder of Python? ")
if answer == 'Guido van Rossum':
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct")
print("You got " + str((score /4) * 100) + "%")
