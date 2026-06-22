from pathlib import Path
from os import getcwd

# check if folders exists
def check_path(path="", folders=[]):
    # one single path to check
    dest_path = Path(path)
    # check if exists
    if dest_path.exists() == False:
        return {"work": False, "value": path}
    

    # check several folders
    for folder in folders:
        # define the path for it
        folder_path = Path(folder)
        # checks if exists
        if folder_path.exists() == False:
            return {"work": False, "value": folder}

   
    # returns true if any path was wrong
    return {"work": True, "value":""}
