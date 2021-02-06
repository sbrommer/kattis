from sys import stdin

s = stdin.readline()

t = s.count('T')
c = s.count('C')
g = s.count('G')

print(t**2 + c**2 + g**2 + 7*min(t, c, g))