import sys

def harshad(n):
    sod = sum(map(int, str(n)))
    return n % sod == 0

n = int(sys.stdin.readline())

while not harshad(n):
    n += 1

print(n)