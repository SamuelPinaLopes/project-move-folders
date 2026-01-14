import sys
import shutil
import os

# function of the program
def get_destination(argments):
    return argments[-2]

def get_folders(argments):
    return argments[-1].split(" ")

def separate_it(argments):
    flags = list()
    directory = list()

    for anything in argments:
        if anything[0] == "-":
            flags.append(anything)
        else:
            directory.append(anything)

    return {"flags": flags, "directories": directory}


# separate flags and directories
flag_and_directory = separate_it(sys.argv[1:])

# where to move
destination = get_destination(flag_and_directory["directories"])

# flags you have
flags = flag_and_directory["flags"]


print(get_folders(flag_and_directory["directories"]))
print(get_destination(flag_and_directory["directories"]))

# move the folder to where you wanted
for folder_move in get_folders(sys.argv[1:]):
    shutil.move(os.getcwd() + '/' + folder_move, destination)
