# @TODO: Your code here
# Info in Dictionaries

## Instructions

# Create a dictionary to store the following:
  # Your pet's name
  # Your pet's age
  # A list of a few of your pet's hobbies
pet_info = {"name": "Flyer", "age": 11, "hobby": ["swimming","playing","sleeping"], "wake_up": {"Monday":"7am","Tuesday":"5am","Friday":"9am"}}
# A dictionary of a few times you wake up during the week
# Print out the following:
# Your pet's name and age.
print(f"My dog, {pet_info['name']} is {pet_info['age']} years old.")
  # How many hobbies your pet has.
print(len(pet_info['hobby']))
  # What your pet's favorite hobby is.
print("My pet's favorite hobby is" + pet_info['hobby'][2])
  # What time your pet wakes on one of the days of the week.
print("My pet sleeps until " + pet_info['wake_up']['Monday'])
