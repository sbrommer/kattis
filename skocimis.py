from sys import stdin

(a, b, c) = list(map(int, stdin.readline().split()))

print(max(b-a, c-b) - 1)
