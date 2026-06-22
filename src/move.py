import argparse
import os
import shutil

inputs = argparse.ArgumentParser(description="Command to move several folders to required destination at once.\n")

# folders and destination
inputs.add_argument("dest", help="Destination for all folders.")
inputs.add_argument("folders", nargs="+", help="Input the folders you want to move.")
# flags
inputs.add_argument("-v", "--verbose", help="See moving folders process working.")
inputs.add_argument("-sf", "--sub-folders", help="Move just subfolders inside folders you passed.")
inputs.add_argument("-f", "--files", help="Move just files from that folders.")
# actually running it
ins = inputs.parse_args()
# move the folder to where you wanted
for folder_move in ins.folders: # for each folder you've got
    path = os.getcwd() + '/' + folder_move # path of current folder to move
    shutil.move(path, ins.dest) # move from current directory to destination
