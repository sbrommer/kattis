from sys import stdin

stdin.readline()
days = list(map(int, stdin.readline().split()))
print(days.index(min(days)))
