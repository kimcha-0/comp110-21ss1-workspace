"""Magic 8 ball demo."""

from random import randint

question: str = input("Ask a yes/no question! ")
response: int = randint(0,2)

is_playing: bool = True
while is_playing:
    if response == 0:
        print("Very doubtful.")
    elif response == 1:
            print("Ask again later.")
    else:
        print("It is certain.")
    
    play_again: str = input("Play again? yes/no ")
    if play_again == "no":
        is_playing = False

print("Have a great day!")