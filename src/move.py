import argparse
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


parse = argparse.ArgumentParser(description="Command to copy several folders at once.", usage="command + flags + destination + folders to move")
parse.add_argument("-v", "--verbose", action="store_true", help="see what is going on while moving")
parse.add_argument("foldername", nargs="+", help="input folders")
parse.add_argument("destination", help="input folders destination")


print(parse.parse_args().foldername)
print(parse.parse_args().destination)








# # move the folder to where you wanted
# for folder_move in folders: # for each folder you've got
    # path = os.getcwd() + '/' + folder_move # path of current folder to move
    # shutil.move(path, destination) # move from current directory to destination

