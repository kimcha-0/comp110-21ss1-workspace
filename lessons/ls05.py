"""looping example."""

i: int = 1
j: int = 0
s: str = ""

while i < 4:
    j = i + j
    s = s + str(i) + str(j)
    i +=1

print (s)