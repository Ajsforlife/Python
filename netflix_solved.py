# Modules
import os
import csv


# Prompt user for video lookup
video = input("What show or movie are you looking for on Netflix? (Please capitalize each word)")

# Set path for file
file_to_load = os.path.join("Resources", "netflix_ratings.csv")

# Open the CSV
with open(file_to_load) as netflix_ratings:

    # Loop through looking for the video
    reader = csv.reader(netflix_ratings)
    header = next(reader)
    for row in reader:
        video_title = row[0]
        rating = row[1]
        user_rating = row[5]
        if video_title == video:
            print(f"{video_title} is rated {rating} with a user rating of {user_rating}.")


