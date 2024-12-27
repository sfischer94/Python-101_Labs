# Reverse the string given below in a single line of code
# with the help of string slicing.

palindrome = "too bad i hid a boot"
n = -1
backwards_string = ""
for i in palindrome:
    backwards_string += palindrome[n]
    n += -1
print(backwards_string)
print(n)