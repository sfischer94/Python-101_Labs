# Take in a number between 1 and 12 from the user
# and print the name of the associated month:
# "January", "February", ... "December"
# Print "Error" if the number from the user is not between 1 and 12.
# Use a nested `if` statement.

num = int(input("Input a number between 1 and 12: "))

# Approach 1: List out each month and use loops or in statement
'''
Jan = "January"
Feb = "February"
Mar = "March"
Apr = "April"
May = "May"
June=  "June"
July = "July"
Aug = "August"
Sept = "September"
Oct =  "October"
Nov = "November"
Dec = "December"

if num == 1:
    print(Jan)
elif num == 2:  
    print(Feb)
elif num == 3:
    print(Mar)
elif num == 4:
    print(Apr)
# and so on
else:
    print("Error")
'''

# Approach 2: Use dictionary
months = {1: "January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}
if num in months:
    value = months[num]
    print(value)
else:
    print("Error")