from math import factorial


def nPr(n, r):
    return factorial(n) // factorial(n - r)


n = int(input())
p = 0

for i in range(1, n + 1):
    p += nPr(n, i)

print(p if p <= 1e9 else 'JUST RUN!!')
