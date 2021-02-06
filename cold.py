import sys

def is_cold(t):
    return t < 0

sys.stdin.readline()

line = sys.stdin.readline()
temps = map(int, line.split())
colds = list(filter(is_cold, temps))

print(len(colds))
