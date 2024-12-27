# Fahrenheit to Celsius:
# ----------------------
# Write the necessary code to convert a degree in Fahrenheit
# to Celsius and print it to the console. Use variable names!

Fahrenheit = int(input("Please input a value in Fahrenheit: "))
Celcius = round(Fahrenheit * (5/9) - 32, 2)
print("The temperature in Celcius is: " + str(Celcius))