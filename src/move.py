#! /usr/bin/env python3

import argparse
from os import getcwd
from shutil import move
from movepy_functions import check_path

# catch parameters passed
inputs = argparse.ArgumentParser(description="Command to move several folders to required destination at once.\nThis command is already recursive, so it doesn't have any recursive flag and won't have.")
# folders and destination
inputs.add_argument("dest", help="Destination for all folders.")
inputs.add_argument("folders", nargs="+", help="Input the folders you want to move.")
# flags
inputs.add_argument("-v", "--verbose", help="See moving folders process working.")
inputs.add_argument("-sf", "--sub-folders", help="Move just subfolders inside folders you passed.")
inputs.add_argument("-f", "--files", help="Move just files from that folders.")
# actually running it
ins = inputs.parse_args()

# checks if the path exists
outpath = check_path(path=ins.dest, folders=ins.folders)
# shows an error if some path is missing or wrong
if outpath['work'] == False:
    print(f"Error: source folder doesn't exist!\nFolder missing: {outpath['value']}")
# move folders if allright 
else:
    # move the folder to where you wanted
    for folder_move in ins.folders: # for each folder you've got
        path = getcwd() + '/' + folder_move # path of current folder to move
        move(path, ins.dest) # move from current directory to destination
