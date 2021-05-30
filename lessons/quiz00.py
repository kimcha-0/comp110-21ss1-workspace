x: int = int(input("Enter a number: "))

if x > 100:
    print("A")
elif x > 90:
    print("B")
    if x > 95: 
        print("C")
elif x > 50:
    print("D")
    if x > 70:
        print("E")
    else:
        print("F")
elif x > 60: 
    print("G")
else: 
    print("H")
print("I")
    