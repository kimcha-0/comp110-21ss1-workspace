# def main() -> None:
#     word: str = input("Enter a word: ")
#     funny: bool = is_funny(word)
#     print(funny)


# def is_funny(word: str) -> bool:
#     if len(word) < 3:
#         return False
#     i: int = 0
#     while i < len(word):
#         if not_funny(word[i]):
#             return False
#         i += 1
#     return True


# def not_funny(char: str) -> bool:
#     return char != "h" and char != "a"


# if __name__ == "__main__":
#     main()
# weight = {"a": 0.0}
# for i in weight:
#     print(type(i))

# a = [10, 20, 30]
# b = [30, 40, 50]
# c = []
# for i in range(len(a)):
#     c.append(a[i] + b[i])

# print(c)

# points = [1, 2, 3]
# print(len(points))
# def sum_list(xs: list[int]) -> int:
#     if len(xs) < 2:
#         return xs[0]
    
#     i: int = 1
#     while i < len(xs):
#         xs[i] = xs[i - 1] + xs[i]
#         i += 1
#     return xs[i - 1]

# def sum_ints(x0: int, x1: int, x2: int) -> int:
#     x1 = x0 + x1
#     x2 = x1 + x2
#     return x2
# points: list[int] = [1, 2, 3]
# total: int

# total = sum_ints(points[0], points[1], points[2])
# print(total)

# total = sum_list(points)
# # print(total)
# l = []
# print(l[0])

def main():
    b = a
    print(b)
    f(a)
    print(b)
    print(a)
    g()
    print(b)
    print(b[0])
    print(a)
    return None

def f(a):
    a[0] = "p"
    a = ["m", "j"]
    print(a)
    return None

def g():
    global a 
    a[1] = "y"
    a = ["k", "g"]
    print(a)
    return None

a = ["w", "u"]

if __name__ == "__main__":
    main()

# def zip_dict(ks, vs):
#     d = {}

#     if len(ks) != len(vs):
#         return d

#     i = 0
#     while i < len(ks):
#         d[ks[i]] = vs[i]
#         i += 1
#     return d

# a = ["ROY", "UNC", "ROY", "UNC"]
# b = ["hi", "W", "bye"]
# c = zip_dict(a, b)
# print(c)