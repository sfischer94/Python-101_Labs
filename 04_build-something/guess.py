# All the text in here are Python code comments.
# A Python code comment starts with a hash symbol (#).
# Python will ignore this when running the file.
# You'll see instructions for your labs written in code comments.
# --------------------------------
# Here's your first task:
# Re-create the guess-my-number game from the course.
# Type the whole code out instead of copy-pasting.
# Typing out code, even if you just copy it, trains your coding skills!
# Write your code below:

import random  #imports package for random

num = random.randint(1,10)  #generate random number between 1 to 10
guess = None  #variable guess

while guess != num:  #as long as the guess doesn't equal the random number, do the following
    guess = input("guess a number between 1 and 10:")  #prompts user to input a number from 1 to 10
    guess = int(guess)  #convert the input number to an integer and assign to the guess variable 
    if guess == num:  #if the guessed number matches the random number
        print("Congratulations! You won!")
        break #end the loop
    else:
        print("Nope. Sorry. Please try again.")
