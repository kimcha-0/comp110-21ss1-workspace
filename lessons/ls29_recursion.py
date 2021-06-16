"""Basic example of a recursive process."""

def yay(x: int) -> None:
    if x > 3:
        print("Base case!")
        return None
    else:
        print(f"Frame: {x}")
        yay(x + 1)
        return None

yay(0)