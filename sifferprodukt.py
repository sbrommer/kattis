from sys import stdin
from operator import mul
from functools import reduce

x = stdin.readline().strip()
digits = list(map(int, x))

while len(digits) > 1:
    digits = filter(lambda d : d != 0, digits)
    digits = reduce(mul, digits)
    digits = [int(d) for d in str(digits)]

print(digits[0])
