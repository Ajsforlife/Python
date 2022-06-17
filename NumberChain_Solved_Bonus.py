# Initial variable to track game play
x = 0
user_play = "y"

# While we are still playing...
while user_play == "y":

    # Ask the user how many numbers to loop through
    numbers = int(input("How many numbers should we go through?"))
   
    # Loop through the numbers. (Be sure to cast the string into an integer.)
    for i in range(x, numbers+x):
        # Print each number in the range
        print(i)

    # Once complete...
    user_play = input("Continue: (y)es or (n)o? ")
    x = numbers + x
    
    