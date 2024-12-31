# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.

import random
answer = int(input("Type in a value between 0 and 1,000,000,000: "))
guess = False

while guess == True:
    for i in range(1,100000001):
        if i == answer:
            guess == True
            break

print(answer)
