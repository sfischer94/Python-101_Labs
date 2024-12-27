# Print out every prime number between 1 and 1000.

# Approach: iterate through list and check for divisibility 
"""prime = []
for num in range(50,60):
    #check if the number being checked is divisible by any number that comes before it from 1 to that number
    prime_check = 0
    for i in range(2,num):
        if num % i == 0:
            prime_check += 1
            break
    #only after going through all the numbers should we confirm the number is a prime number
    if prime_check == 0:
        prime.append(num)
print(prime)"""


# Alternative: Find composite numbers and remove them from a list with the range of numbers
numbers = range(50,60)
num_list = list(numbers)
composite = []
for num in numbers:
    #check if the number being checked is divisible by any number that comes before it from 1 to that number
    for i in range(2,num):
        if num % i == 0:
            composite.append(num)
            break

#Remove overlapping numbers from composite and list of numbers in the range
for n in composite:
    num_list.remove(n)
print(num_list) #Prime numbers
