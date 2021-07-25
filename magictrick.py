from sys import stdin

s = stdin.readline().strip()

print(1 if len(set(s)) == len(s) else 0)
