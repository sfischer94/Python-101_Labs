# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4

phrase = input("Type in something using alphabetic characters: ")

"""while phrase.isalpha == False:
    try:
        phrase.isalpha()
        break   
    except AttributeError:
        input("That isn't a valid reply. Please input a response: ")"""

search = input("Please input a letter to search for in the phrase: ")

#Approach 1: Find function
location = phrase.find(search)
print(location)

# Approach 2: Loop
"""i = 0
if search not in phrase:
    print("Sorry, that letter isn't in the phrase.")

for letter in phrase.lower():
    i += 1
    if letter == search.lower():
        print(i)
        break"""



