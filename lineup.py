from sys import stdin

n = int(stdin.readline())

names = []

for _ in range(n):
    names.append(stdin.readline())

if names == sorted(names):
    print('INCREASING')
elif names == sorted(names, reverse=True):
    print('DECREASING')
else:
    print('NEITHER')
