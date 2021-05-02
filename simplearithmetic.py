from sys import stdin
from decimal import Decimal

a, b, c = list(map(int, stdin.readline().split()))

a = Decimal(a)
b = Decimal(b)
c = Decimal(c)

print(a * b / c)
