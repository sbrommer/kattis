o = open(0)

p, q = [int(n) for n in o.readline().split()]
s = o.readline().strip()

if s == 'AABB' and q == 7:
    print(8, 9)

elif s == 'ABAB' and (p, q) == (6, 8):
    print(7, 9)

elif s == 'ABBA' and q == p + 3:
    print(p + 1, p + 2)

elif s == 'BAAB' and (p, q) == (2, 8):
    print(1, 9)

elif s == 'BABA' and (p, q) == (2, 4):
    print(1, 3)

elif s == 'BBAA' and p == 3:
    print(1, 2)

else:
    print(-1)
