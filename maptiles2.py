from sys import stdin

s = stdin.readline().strip()

z = len(s)

print(z, end=' ')

x = 0
y = 0

for q in s:
    x *= 2
    y *= 2
    
    q = int(q)
    if q % 2 == 1:
        x += 1
    if q == 2 or q == 3:
        y += 1

print(x, y)