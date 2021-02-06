import sys

line = sys.stdin.readline()
(x, y, n) = map(int, line.split())

for i in range(1, n+1):
    s = ''

    if i % x == 0:
        s += 'Fizz'
    if i % y == 0:
        s += 'Buzz'

    print(i if s == '' else s)

