from sys import stdin

s = int(stdin.readline())

print(str(s) + ':')

for x in range(2, s):
    y = x - 1
    if s % (x + y) == 0:
        print(str(x) + ',' + str(y))
    if (s-x) % (x + y) == 0:
        print(str(x) + ',' + str(y))
    if s % x == 0:
        print(str(x) + ',' + str(x))