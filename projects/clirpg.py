# Build a CLI RPG game following the instructions from the course.

# Ask the player for their name.

# Display a message that greets them and introduces them to the game world.

# Present them with a choice between two doors.

# If they choose the left door, they'll see an empty room.

# If they choose the right door, then they encounter a dragon.
 
# In both cases, they have the option to return to the previous room or interact further.

# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.

# When encountering the dragon, they have the choice to fight it.

# If they have the sword from the other room, then they will be able to defeat it and win the game.

# If they don't have the sword, then they will be eaten by the dragon and lose the game.


# Creating variables
sword = False
Door_Left = None
Door_Right = None


name = input("Please state your name: ")
Lobby = True
print("Welcome to the game " + name + "!")
print("You've landed in a dungeon of a castle. There are two doors to choose from: the left door or the right door. Which one will you choose?")

while Lobby == True:
    choice = ((input("Input 'LEFT' or 'RIGHT' to choose which door: ")).upper())

    if choice == "LEFT":
        Door_Left = True
        Lobby = False
        print("\n" + "You've entered the left door to find an empty room. Not much to see here.")
        search_choice = input("Would you like to take a look around? Type in 'YES' to look around or 'NO' to return to the previous room: ").upper()
        
        while search_choice != "YES" and search_choice != "NO":
            print("Sorry, that's not an option.")
            search_choice = input("Would you like to take a look around? Type in 'YES' to look around or 'NO' to return to the previous room: ").upper()
        
        if search_choice == "YES":
            if sword == False:
                print("\n" + "You take a look around the room and find a sword!")
                sword_choice = input("Would you like to take it or leave it? Type in 'LEAVE' or 'TAKE': ").upper()

                while sword_choice != "LEAVE" and sword_choice != "TAKE":
                    print("\n" + "Sorry, that's not an option.")
                    sword_choice = input("Would you like to take it or leave it? Type in 'LEAVE' or 'TAKE': ").upper()

                if sword_choice == "LEAVE":
                    print("\n" + "You have left the sword and returned to the previous room." + "\n")
                    Door_Left = False
                    Lobby = True
                    continue
                elif sword_choice == "TAKE":
                    sword = True
                    print("\n" + "You have taken the sword and returned to the previous room." + "\n")
                    Door_Left = False
                    Lobby = True
                    continue
            elif sword == True:
                print("\n" + "There's nothing else around here. You return to the prevous room." + "\n")
                Door_Left = False
                Lobby = True
        
        elif search_choice == "NO":
            Door_Left = False
            Lobby = True
            print("\n" + "You have returned to the previous room." + "\n")

    elif choice == "RIGHT":
        Door_Right = True
        Lobby = False
        print("\n" + "You have entered the right door and come to a dark room...and then, you hear a deep growl and two bright eyes appear. The beast roars and you realize you've encountered a dragon!!")
        choice = input("Will you choose to fight it or return to the previous room? Type 'FIGHT' or 'RETURN': ").upper()
        print(choice)
        
        while choice != "FIGHT" and choice != "RETURN":
            print("\n" + "Sorry that's not an option.")
            choice = input("Will you choose to fight it or return to the previous room? Type 'FIGHT' or 'RETURN': ").upper()
        if choice == "FIGHT":
            if sword == True:
                print("\n" + "Congratulations, you've slayed the dragon! You win!!")
                break
            if sword == False:
                print("\n" + "You fight mightily, but the dragon crushes you and swallows you whole. You have lost :(")
                break
        elif choice == "RETURN":
            Door_Right = False
            Lobby = True
            print("\n" + "You have returned to the previous room." + "\n")
        else:
            print("Sorry that's not an option.")

    else:
        print("\n" + "Sorry, that's not an option. Please pick a door.")