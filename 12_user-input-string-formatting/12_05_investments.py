# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.

amount = input("Input the amount you'd like to invest: ")
amount = int(amount)

rate = input("What interest rate would you like to invest at? Enter the number as a percentage: ")
rate = int(rate)

years = input("How many years will you be investing? ")
years = int(years)

interest = amount*(rate/100)*years
total = amount + interest
print("The interest accrued will be " + str(interest))
print("The future value will be " + str(total))


