"""Exploring command line arguments."""

# gives us access to the arguments our program begins with
import sys

# argv is just the list of arguments our program is begun with
# by default, when you begin a program from the command line
# the first argument is the file you are trying to run
args: list[str] = sys.argv
print(len(args))
print(args[1])
print(args[2])

# spaces between words determine the separation of arguments
# can put quotes to a have a multiple word argument

# Specify the problem we want to solve
# run our program as a module with two command line arguments
# 1. name of the file we'd like to search
# 2. search term we are looking for
# print out all the lines containing the search term and
# give the total number of matches
def read_args() -> dict[str, str]:
    """Check for valid CLI arguments and return them in a dictionary."""
    if len(sys.argv) != 3:
        print("usage: python -m lessons.ls27_cli_args [file] [keyword]")
        exit()
    return {
        "file_path": sys.argv[1],
        "keyword": sys.argv[2]
    }


def search_file(file_path:str, keyword: str) -> list[str]:
    """Open a file, read each line, return matching lines."""
    matches: list[str] = []
    file_handle = open(file_path, "r", encoding="utf-8")
    for line in file_handle:
        if keyword in line:
            matches.append(line)
    file_handle.close()
    return matches


def show_results(matches: list[str]) -> None:
    """print out matches and total number of matches."""
    for line in matches:
        print(line)
    print(f"Total number of matches {len(matches)}")
    return None

def main() -> None:
    """Entrypoint."""
    args: dict[str, str] = read_args()
    results: list[str] = search_file(args["file_path"], args["keyword"])
    show_results(results)
    return None

if __name__ == "__main__":
    main()