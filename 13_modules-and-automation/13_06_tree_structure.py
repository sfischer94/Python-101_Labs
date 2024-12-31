# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.

import pathlib

location = pathlib.Path(r"C:\Users\StephenFischer\Documents\CodingNomads\Python_101\Labs")
for file in location.rglob("*"):
    if file.suffix == ".py":
        print(file)