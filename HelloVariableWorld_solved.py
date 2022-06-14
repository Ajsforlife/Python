# Create a variable called 'name' that holds a string
name = str(input("What is your name?"))

# Create a variable called 'country' that holds a string
country = str(input("Where are you from?"))

# Create a variable called 'age' that holds an integer
age = int(input("How old are you?"))

# Create a variable called 'hourly_wage' that holds an integer
hourly_wage = int(input("How much do you make per hour?"))

# Calculate the daily wage for the user
daily_wage = hourly_wage * 8

# Create a variable called 'satisfied' that holds a boolean
satisfied = bool(input("Were you satisfied?")) 

# Print out "Hello <name>!"
print("Hello " + name)

# Print out what country the user entered
print(country)

# Print out the user's age
print(age)

# With an f-string, print out the daily wage that was calculated
print(f"{name} makes {daily_wage}$ per day.")

# With an f-string, print out whether the users were satisfied
print(f"The user was satisfied: {satisfied}")

