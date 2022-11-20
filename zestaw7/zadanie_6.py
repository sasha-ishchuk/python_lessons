import itertools
import random

iter1 = itertools.cycle([0, 1])
for i in iter1:
    print(i, end=", ")

iter2 = iter(lambda: random.choice(["N", "E", "S", "W"]), 0)
for i in iter2:
    print(i, end=" ")

iter3 = itertools.cycle([0, 1, 2, 3, 4, 5, 6])
for i in iter3:
    print(i, end=", ")
