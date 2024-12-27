# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.

phrase = input("Give me your honest opinion of this program: ")

i = 1
new_phrase = ""
for char in phrase:
    if char.isspace() == True:
        new_phrase += char
    if char.isalpha() == True:
        if i % 2 == 0:
            new_phrase += char.upper()
        else:
            new_phrase += char
        i += 1
print(new_phrase)

