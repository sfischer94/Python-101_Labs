# Write a Hangman game in Python.
# Users should have a limited amount of attempts to guess a pre-defined word.
# Print feedback to the user when they made a guess,
# and keep track of and communicate their remaining attempts.

# Hard-code a word that needs to be guessed in the script
word = "lamp".lower()
display_word = ""
for i in word:
    display_word += "_"
solved = False
used_letters = []

# Print an explanation to the user
print("""Hello, we're going to play Hangman!
You'll be presented with a mystery word that you'll have to guess the letters to.
Each try you get to guess 1 letter.
You have 6 tries to guess all the letters in the word or else you lose.

Ready to play? Let's go!""" + "\n")

# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"
print("Here's the word: " + display_word + "\n")

# Create a counter for how many tries a user has
incorrect = 0

# Ask for user input
while solved == False:
    guess = input("Guess a letter: ").lower()

# Allow only single-character alphabetic input
    while len(guess) > 1:
        guess = input("That's too long. Please guess a single letter: ")
    while guess.isalpha() == False:
        guess = input("That's not a single letter guess. Please guess a single letter: ")
    while guess in used_letters:
        guess = input("You've already used that letter. Try another one: ")

# Keep asking them for their guess until they won or lost

# When they find a correct character, display the blank with the word
#   filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"

    # String slicing to change display word
    start_display = display_word
    char_count = 0
    for char in word:
        if guess == char:
            display_word = display_word[:char_count] + guess + display_word[char_count + 1:]
        char_count += 1
    print(display_word)

    # Add guessed letter to the used list
    used_letters.append(guess)

    # If the display word has not changed (i.e. no replacement), add 1 to incorrect answer counter
    if start_display == display_word: 
        incorrect += 1

# Display a winning message and the full word if they win
    # Check if there are no more underscores in the display word
    if "_" not in display_word: 
        print("Congratulations! You win!")
        solved = True
        break

# Display a losing message and quit the game if they don't make it
    if incorrect == 6:
        print("Sorry, you lose.")
        break




    



