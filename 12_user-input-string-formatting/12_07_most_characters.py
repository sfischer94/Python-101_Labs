# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings

first = input("Please input your first phrase: ")
second = input("Please input your second phrase: ")
third = input("Please input your third phrase: ")

phrases = [first, second, third]
long_length = max(len(i) for i in phrases)
long_word = max(i for i in phrases)

print(long_length, long_word)

