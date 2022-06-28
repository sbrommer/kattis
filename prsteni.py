from fractions import Fraction

input()
r1, *rs = map(int, input().split())

for r in rs:
    f = Fraction(r1, r)
    print(f.numerator, '/', f.denominator, sep='')
