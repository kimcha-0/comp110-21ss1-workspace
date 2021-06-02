# """Examples of dictionaries."""

# # Establish a type with the following syntax
# # dict[key type, value type]
# # empty dictionary literal is { }
# players: dict[str, int] = {}

# # Insert a new key-value pair
# players["Brooks"] = 15
# # Reference keys inside subscription notation, associated 
# # values are assigned on RHS of assignment operator
# players["Love"] = 2
# players["Bacot"] = 4
# players["Bacot"] += 1
# print(players)

new_dict: dict[str, str] = {"Kaki": "blue", "Lasya": "blue"}
new_dict["Matt"] = "Red"
print(new_dict)

for cookie in new_dict:
    print(f"The key is {cookie} and the value is {new_dict[cookie]}")
for val in new_dict.values():
    print(f"the value is {val}")

def passes(students: dict[str, float]) -> list[str]:
    """Given student info, who passes?"""
    result: list[str] = []
    for student in students:
        if students[student] > 60:
            result.append(student)
    return result

s: dict[str, float] = {"Andrew": 100.0, "Shaurik": 89.0, "Claire": 40.0}
print(passes(s))
