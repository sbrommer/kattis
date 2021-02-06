import sys

remainders = set()

for _ in range(10):
    a = int(sys.stdin.readline())
    remainders.add(a % 42)

print(len(remainders))