import sys

n = int(sys.stdin.readline())

print(int(bin(n)[:1:-1],2))
