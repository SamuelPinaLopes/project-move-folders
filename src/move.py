import argparse

parse = argparse.ArgumentParser(description="Command to copy several folders at once.")

parse.add_argument("-v", "--verbose", action="store_true", help="see what is going on while moving")
parse.add_argument("dest", help="input the folders destination")
parse.add_argument("folder", nargs="+", help="input your folders")

args = parse.parse_args()

if args.verbose == True:
    for folders in args.folder:
        print(folders)
    print("\n\ndestination of folders: ", args.dest)
    print("verbose flag added: ", args.verbose)

else:
    print("you don't have to see anything if you didn't put the flag...\n\n:<")
