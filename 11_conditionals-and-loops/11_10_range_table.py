# Read up on `range()` and additional options for `print()`.
# Then use a loop to print the following table to the console:
#
# 0 1 2 3 4 5 6 7 8 9
# 10 11 12 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26 27 28 29
# 30 31 32 33 34 35 36 37 38 39
# 40 41 42 43 44 45 46 47 48 49

print(*range(0,10)) #Using the unpacking operator *
for i in range(10,20):
    print(i, end = ' ') #Using the end parameter in print function
print("\n" + ' '.join(str(i) for i in range(20,30))) # Adding a new line and then iterating over a range + convert to string and joining to convert the generator object
print(*range(40,50))