# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please

phrase = input("Type in something using alphabetic characters: ")
symbol = input("Please input a symbol to search for in the phrase: ")
#while symbol.isspace() is False:
#    print("no")

# Approach 1: Replace function
replacement_letter = phrase[0]
new_phrase = phrase.replace(replacement_letter, "$")
print(new_phrase)

#Approach 2: Loop through
"""new_phrase = ""
i = 0
for letter in phrase:
    i += 1
    if letter == replacement_letter:
        new_phrase += symbol
    else:
        new_phrase += letter

print(new_phrase)"""


