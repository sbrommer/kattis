from sys import stdin

(x, y) = list(map(int, stdin.readline().split()))

print('possible' if y % 2 == 0 else 'impossible')
