from sys import stdin

stones = stdin.readline()

w = stones.count('W')
b = stones.count('B')

print(1 if w == b else 0)
