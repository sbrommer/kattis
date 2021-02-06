import sys

line = sys.stdin.readline()[:-1]

n = len(line)

l1 = '.'
l2 = '.'
l3 = '#'

for i in range(1, n+1):
    c = '*' if i % 3 == 0 else '#'
    d = c

    if i < n and (i+1) % 3 == 0:
        d = '*'

    l1 += '.' + c + '..'
    l2 += c + '.' + c + '.'
    l3 += '.' + line[i-1] + '.' + d

print(l1)
print(l2)
print(l3)
print(l2)
print(l1)