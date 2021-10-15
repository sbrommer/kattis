from sys import stdin
from math import gcd

def lcm(c1, c2):
    return (c1 * c2) / gcd(c1, c2)

k = int(stdin.readline())

first = float('inf')
for _ in range(k):
    y, c1, c2 = list(map(int, stdin.readline().split()))
    first = min(first, y + lcm(c1, c2))

print(int(first))
