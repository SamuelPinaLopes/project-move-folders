# project-move-folders
My mission with this projects is create a really simple way to move a lot of folders into a target directory.
Basically this tool moves multiple foldes into a target directory using a simple command.


It is recommended to handle potential exceptions such as FileNotFoundError or PermissionError using try-except blocks, especially when dealing with file operations that depend on system access rights.
Additionally, ensure the destination directory exists or is correctly specified to avoid errors during the move operation.

Syntax: shutil.move(source, destination)

source: Path to the folder you want to move (string or pathlib.Path).

destination: Target directory path where the folder should be moved.

Behavior:
If the destination is an existing directory, the source folder is moved inside it.
If the destination does not exist, the folder is moved and renamed to the destination name.
Any non-existent intermediate directories in the destination path are created automatically.

Return Value: The function returns the new path of the moved folde

# what to do more
# write the program receive more than one folder in one time.
# write the program (with parameters) that stores and enumerates the default locations.
# show the files being moved with an little animation in command prompt.
