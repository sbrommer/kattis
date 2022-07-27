from operator import mul
from functools import reduce

x = input()
digits = list(map(int, x))

while len(digits) > 1:
    digits = filter(lambda d: bool(d), digits)
    digits = reduce(mul, digits)
    digits = [int(d) for d in str(digits)]

print(digits[0])
