# Write a script that searches a folder you specify (as well as its subfolders, up
# to two levels deep) and compiles a list of all `.jpg` files contained in there.
# The list should include the complete path of each `.jpg` file.
# 
# You should train:
# 
# - Using `for` loops
# - Using conditional statements
# - Working with `pathlib`
# - Thinking about nested loops
# 
# If you are feeling bold, create a list containing each type of file extension
# you find in the folder.
# Start with a small folder to make it easy to check whether your program is
# working correctly. Then search a bigger folder.
# This program should work for any specified folder on your computer.

import pathlib

path = pathlib.Path(r"C:\Users\StephenFischer\OneDrive - SolidProfessor\Pictures")
jpeg_files = []
filetypes = []

for file in path.glob('*/*/*'):
    if file.suffix == ".jpg":
        jpeg_files.append(file)
    if file.suffix not in filetypes:
        filetypes.append(file.suffix)

for i in jpeg_files:
    print(i)
print(filetypes)


