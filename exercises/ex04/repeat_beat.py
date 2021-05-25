"""Repeating a beat in a loop."""

__author__ = "730407570"


# Begin your solution here...
beat: str = input("What beat do you want to repeat? ")
repeat_num: int = int(input("How many times do you want to repeat it? "))

total_beat: str = beat

if repeat_num <= 0:
    print("No beat...")
else:
    while repeat_num > 1:
        total_beat = total_beat + " " + beat
        repeat_num -= 1
    print(total_beat)