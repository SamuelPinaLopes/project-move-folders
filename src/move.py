import sys
import shutil
import os

# function of the program
def get_destination(argments):
    return argments[0] # destination has to be always the first element in dictionary (you'll recieve one list here)

def get_folders(argments):
    return argments[-1].split(" ") # get the last list with folders and split it. 

def separate_it(argments): # separates flags and directories 
    flags = list() # list of flags
    directory = list() # list of directories (both, destination and path)

    for anything in argments: # does that
        if anything[0] == "-": # checks if it is a flag appends it in flag else appends it in directory
            flags.append(anything)
        else:
            directory.append(anything)

    return {"flags": flags, "directories": directory} # returns a dictionary


# separate flags and directories
flag_and_directory = separate_it(sys.argv[1:])

# where to move
destination = get_destination(flag_and_directory["directories"]) # list output

# folders to move
folders = get_folders(flag_and_directory["directories"])

# gets the flags you have
flags = flag_and_directory["flags"] # list output

# move the folder to where you wanted
for folder_move in folders: # for each folder you've got
    path = os.getcwd() + '/' + folder_move # path of current folder to move
    shutil.move(path, destination) # move from current directory to destination