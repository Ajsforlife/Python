# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
if user_choice == computer_choice:
    print("The user and the computer both chose," + user_choice, " You Tied!")
elif user_choice == "r":
    if computer_choice == "s":
        print("The user chose rock, and the computer chose scissors, You Win!")
elif user_choice == "r":
    if computer_choice == "p":
        print("The user chose rock, and the computer chose paper, You Win!")
elif user_choice == "s":
    if computer_choice == "p":
        print("The user chose scissors, and the computer chose paper, You Win!")
else:
    print("You lose! The computer beat you!")
