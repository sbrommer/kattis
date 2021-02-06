import sys

def read(s):
    return int(s[::-1])

line = sys.stdin.readline()
(a, b) = map(read, line.split())

print(max(a, b))
