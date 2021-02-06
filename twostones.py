import sys

n = int(sys.stdin.readline()[:-1])

print("Bob" if n % 2 == 0 else "Alice")

