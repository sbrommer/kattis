from sys import stdin
from fractions import Fraction

stdin.readline()
r1,*rs = list(map(int, stdin.readline().split()))

for r in rs:
    f = Fraction(r1,r)
    print(f.numerator, '/', f.denominator, sep='')
