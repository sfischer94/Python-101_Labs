# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.

# Approach 1: Multiple if loops
'''
a,e,i,o,u,y = 0,0,0,0,0,0
phrase = input("Type in a phrase: ")
for letter in phrase.lower():
    if letter == "a":
        a += 1
    if letter == "e":
        e += 1
    if letter == "i":
        i += 1
    if letter == "o":
        o += 1
    if letter == "u":
        u += 1
    if letter == "y":
        y += 1

print(f"""Here's the count of each vowel: \n
      A: {a} \n
      E: {e} \n
      I: {i} \n
      O: {o} \n
      U: {u} \n
      Y: {y}""")
'''

# Approach 2: Using dictionary
vowels = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0, 'y':0}
phrase = input("Type in a phrase: ")
for letter in phrase.lower():
      if letter in vowels:
            vowels[letter] += 1
print(vowels)
