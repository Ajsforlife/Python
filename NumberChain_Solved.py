# Initial variable to track game play
user_play = "y"

# While we are still playing...
while user_play == "y":

    # Ask the user how many numbers to loop through
    numbers = int(input("How many numbers should we go through?"))
    
    # Loop through the numbers. (Be sure to cast the string into an integer.)
    for i in range(1, numbers+1):


        # Print each number in the range
        print(i)

    # Once complete...
    user_play = input("Continue: (y)es or (n)o? ")