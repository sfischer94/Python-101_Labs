# Move and rename all .png files on your Desktop

# Identify all screenshots on your Desktop

# Create a new directory

# Move and rename all screenshots

import pathlib
path = pathlib.Path(r"C:\Users\StephenFischer\OneDrive - SolidProfessor\Desktop") #Returns the path of your current working directory

directory = pathlib.Path(r"C:\Users\StephenFischer\OneDrive - SolidProfessor\Desktop\PNG_Files") #Define new file path
directory.mkdir(exist_ok=True)

count = 0
for filepath in path.iterdir():
# Filter for screenshots only
    if filepath.suffix == ".png":
        count += 1
        # Replace file with new name and move to directory
        new_filepath = directory.joinpath("Image " + str(count))
        filepath.replace(new_filepath)
        print(new_filepath.name)

