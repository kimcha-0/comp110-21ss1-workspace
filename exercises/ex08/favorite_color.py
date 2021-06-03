"""A program to determine top favorite colors."""

__author__ = "730407570"


from typing import ItemsView


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    # TODO 2: Test your functions here
    s: dict[str, str] = {"Max": "blue", "David": "yellow", "Sahil": "red", "Abhi": "blue", "Kaylan": "yellow", "Suraj": "yellow"}
    print(favorite_color(s))
    return None


# TODO 1: Define the favorite_color function, and its logic, here.
def favorite_color(x: dict[str, str]) -> str:
    frequency_table: dict[str, int] = {}
    for i in x:
        if x[i] in frequency_table:
            frequency_table[x[i]] += 1
        else:
            frequency_table[x[i]] = 1
    frequency_list: list[int] = []
    for color in frequency_table:
        frequency_list.append(frequency_table[color])
    result: int = frequency_list[0]
    for item in frequency_list:
        if item > result:
            result = item
    max_color_value: int = result
    for i in frequency_table:
        if frequency_table[i] == max_color_value:
            return i
    return i

if __name__ == "__main__":
    main()