# user_input.py

# Asking user for their name and storing it in a variable called "name"
name = input("What is your name? ")

# Asking user for their age and storing it in a variable called "age"
age = input("How old are you? ")

# Asking user for their location and storing it in a variable called "location"
location = input("Where do you live? ")

# Printing out a personalized message using the user's name, age, and location
print("Hello {}, you are {} years old and live in {}.".format(name, age, location))
