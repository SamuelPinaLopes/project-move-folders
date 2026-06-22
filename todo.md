Things to add!

- relative paths;
- folder names but without needing to put this => ";
- error catches;
- handle flags;

argparse / proper CLI parsing

replace manual sys.argv parsing ✅
support --help ✅
support flags like -v, -r, --dry-run ✅

error handling

detect missing destination or folders ✅
check if source folder exists ✅
check if destination exists and is writable
catch shutil.move failures and report them

path support

support absolute paths
support relative paths
normalize paths with os.path.abspath() or pathlib

folder selection

allow multiple folder names without requiring quotes
support wildcard patterns like *.txt or folder*
allow moving a single folder or many folders

helpful user output

add a verbose mode
print what will be moved
add a dry-run option so users can preview actions without moving

tests and documentation

add tests for parsing, validation, and moving logic
update Readme.md with usage examples
document required syntax and flags

safer behavior

avoid hardcoding os.getcwd() + '/'
use pathlib.Path
do not overwrite existing destination unintentionally
optionally prompt before overwriting

