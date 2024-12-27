# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.

name = input("What is your name? ")

#Approach 1: use For loop and check for space to split the name
"""firstname = ""
for letter in name:
    if letter.isspace():
        break
    else:
        firstname += letter
print("Welcome to this program " + firstname + "!")"""

#Approach 2: use the Split function
name.split()
firstname = name.split()[0]
print("Welcome to this program " + firstname + "!")
