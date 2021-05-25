"""Magic 8 ball demo."""

from random import randint

question: str = input("Ask a yes/no question! ")
response: int = randint(0,2)

if response == 0:
    print("Very doubtful.")
else:
    if response == 1:
        print("Ask again later.")
    else:
        print("It is certain.")