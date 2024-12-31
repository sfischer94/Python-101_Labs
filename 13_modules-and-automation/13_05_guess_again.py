# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.

import random

used_numbers = []
num = random.randint(1,10)
tries = 0


while True:
    while True:
        guess = input("Try to guess a number between 1 and 10: ")
        try:
            int(guess)
            break
        except ValueError:
            print("That's not a number.", end=" ")
            continue
    if int(guess) not in range(1,11):
        print("That's not in range.", end=" ")
        continue
    if guess in used_numbers:
        print("You've already tried that number. Please try another number.", end=" ")
        continue

    tries += 1
    if int(guess) != num:
        if tries == 3:
            print("Sorry, that's not correct. You lose.", end=" ")
            break
        else:
            print("Sorry, that's not correct.", end=" ")
            used_numbers.append(guess)
            continue
    if int(guess) == num:
        print("Congratulations! You won!")
        break


