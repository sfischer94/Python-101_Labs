# Write a script that moves all files with the .png extension
# from one folder to another

# Import pathlib
import pathlib

# Find the path to my Desktop
path = pathlib.Path(r"C:\Users\StephenFischer\OneDrive - SolidProfessor\Desktop") #Returns the path of your current working directory
print(path.name)

# Create a new folder
new_path = pathlib.Path(r"C:\Users\StephenFischer\OneDrive - SolidProfessor\Desktop\Screenshots") #Define new file path
new_path.mkdir(exist_ok=True)

# Filter for screenshots only
for filepath in path.iterdir():
    if filepath.suffix == ".png":
# Create a new path for each file
        new_filepath = new_path.joinpath(filepath.name)
# Move the screenshot there
        filepath.replace(new_filepath)