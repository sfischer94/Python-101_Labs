# Use Python's string mini-language to display the table
# that you've built before in a slightly better formatted manner:
#
#  0  1  2  3  4  5  6  7  8  9
# 10 11 12 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26 27 28 29
# 30 31 32 33 34 35 36 37 38 39
# 40 41 42 43 44 45 46 47 48 49

# Approach 1: Series of for loops with different ranges and print statements followed by line break
'''
for i in range(0,10):
   print(f"{i}", sep=' ', end=' ')
print("")
for i in range(10,20):
   print(f"{i}", sep=' ', end=' ')
print("")
for i in range(20,30):
   print(f"{i}", sep=' ', end=' ')
print("")
for i in range(30,40):
   print(f"{i}", sep=' ', end=' ')
print("")
for i in range(40,50):
   print(f"{i}", sep=' ', end=' ')
'''

# Approach 2: Range object and iterate through with for loop and if loop to check for boundaries
'''
nums = range(0,50)
for i in nums:
    if i > 0 and i % 10 == 0:
        print("\n")
    print(i, end=" ")
'''

# Approach 3: Multiple print statements with different ranges
'''
print(" ".join(str(i) for i in range(0,10)))  # Using .join to concatenate and iterating thru generator object with string conversion
print(" ".join(str(i) for i in range(10,20)))
print(" ".join(str(i) for i in range(20,30)))
print(" ".join(str(i) for i in range(30,40)))
print(" ".join(str(i) for i in range(40,50)))
'''