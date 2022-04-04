from sys import stdin

r, c = list(map(int, stdin.readline().split()))

print(100 * (r-c)**2 / r**2)
