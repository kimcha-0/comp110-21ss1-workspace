import os

def traverse(path: str) -> None:
    """Print and traverse contents at some location in our file system."""
    if os.path.isfile(path):
        print(f"file: {path}")
        return None
    else:
        # recursive case
        # when the path refers to a directory name
        print(f"directory: {path}")
        for child_path in os.listdir(path):
            traverse(os.path.join(path, child_path))

traverse("exercises")