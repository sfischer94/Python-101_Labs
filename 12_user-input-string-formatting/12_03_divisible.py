# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.

while True:
    try:
        num = int(input("Type in a number between 1 and 1,000,000,000: "))
        break
    except ValueError:
        print("That's not a valid number. Please input a number between 1 and 1,000,000,000: ")

if int(num) % 3 != 0:
    print("That number is not divisible by 3. The result is " + str(int(num)/3))
else:
    print("That number is divisible by 3. The result is " + str(int(num)/3))
